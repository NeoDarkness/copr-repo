#!/usr/bin/env bash

# Auto sync RPM spec versions using git remote
# Supports:
# - Stable releases via git tags
# - Snapshot packages via HEAD commit
# - Postman special release API
# - Auto Cargo vendor generation for Rust packages

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

UPDATED=0
TIMEOUT=15

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m'

# --------------------------------------------------
# Spec helpers
# --------------------------------------------------

get_spec_version() {
    awk '
        /^Version:/ {
            sub(/^Version:[[:space:]]*/, "")
            print
            exit
        }
    ' "$1"
}

get_spec_url() {
    awk '
        /^%global[[:space:]]+forgeurl/ {
            print $3
            exit
        }

        /^URL:/ {
            sub(/^URL:[[:space:]]*/, "")
            print
            exit
        }
    ' "$1"
}

get_spec_commit() {
    awk '
        /^%global[[:space:]]+commit/ {
            print $3
            exit
        }
    ' "$1"
}

is_forge_snapshot() {
    grep -q "^%global[[:space:]]\+commit" "$1"
}

is_rust_package() {
    grep -Eiq "cargo|rust" "$1"
}

# --------------------------------------------------
# Git helpers
# --------------------------------------------------

get_latest_commit() {
    timeout "$TIMEOUT" \
        git ls-remote "$1" HEAD 2>/dev/null \
        | awk '{print $1}'
}

get_latest_tag() {
    timeout "$TIMEOUT" \
        git ls-remote --tags --refs "$1" 2>/dev/null \
        | awk -F/ '{print $3}' \
        | grep -Ev '\^\{\}$' \
        | sed 's/^v//' \
        | sort -V \
        | tail -n1
}

# --------------------------------------------------
# Special handlers
# --------------------------------------------------

get_postman_version() {
    timeout "$TIMEOUT" curl -fsSL \
        "https://www.postman.com/mkapi/release.json" \
        | jq -r '.notes[0].version // empty'
}

# --------------------------------------------------
# Updaters
# --------------------------------------------------

update_version() {
    local spec="$1"
    local version="$2"

    sed -i -E \
        "s|^Version:[[:space:]]+.*|Version:        $version|" \
        "$spec"

    sed -i -E \
        "s|^Release:[[:space:]]+.*|Release:        %autorelease|" \
        "$spec"
}

update_git_snapshot() {
    local spec="$1"
    local commit="$2"

    sed -i -E \
        "s|^%global[[:space:]]+commit[[:space:]]+.*|%global commit $commit|" \
        "$spec"
}

# --------------------------------------------------
# Cargo vendor
# --------------------------------------------------

generate_cargo_vendor() {
    local pkg_dir="$1"
    local version="$2"
    local url="$3"

    local vendor_tarball="$pkg_dir/vendor.tar.gz"

    if [[ -f "$vendor_tarball" ]]; then
        return 0
    fi

    if ! command -v cargo >/dev/null 2>&1; then
        echo -e "  ${RED}⚠ cargo not found${NC}"
        return 1
    fi

    echo -e "  ${BLUE}📦 Generating Cargo vendor...${NC}"

    local tmp_dir
    tmp_dir="$(mktemp -d)"

    rm -f "$vendor_tarball"

    if git clone \
        --depth 1 \
        --branch "v$version" \
        "$url" \
        "$tmp_dir/src" >/dev/null 2>&1; then

        pushd "$tmp_dir/src" >/dev/null

        if cargo vendor "$tmp_dir/vendor" >/dev/null 2>&1; then
            tar -czf "$vendor_tarball" -C "$tmp_dir" vendor

            echo -e "  ${GREEN}✨ vendor.tar.gz generated${NC}"

            UPDATED=$((UPDATED + 1))
        else
            echo -e "  ${RED}⚠ cargo vendor failed${NC}"
        fi

        popd >/dev/null
    else
        echo -e "  ${RED}⚠ git clone failed${NC}"
    fi

    rm -rf "$tmp_dir"
}

# --------------------------------------------------
# Main
# --------------------------------------------------

echo -e "${BLUE}🔍 Syncing package versions...${NC}\n"

for dir in "$REPO_ROOT"/*; do
    [[ -d "$dir" ]] || continue

    pkg="$(basename "$dir")"

    case "$pkg" in
        .git|scripts|.github)
            continue
            ;;
    esac

    spec="$dir/$pkg.spec"

    [[ -f "$spec" ]] || continue

    echo -e "${YELLOW}Checking $pkg...${NC}"

    version="$(get_spec_version "$spec")"
    url="$(get_spec_url "$spec")"

    echo "  Current: $version"

    # --------------------------------------------------
    # Snapshot packages
    # --------------------------------------------------

    if is_forge_snapshot "$spec"; then
        commit="$(get_spec_commit "$spec")"
        latest="$(get_latest_commit "$url" || true)"

        if [[ -z "$latest" ]]; then
            echo -e "  ${RED}⚠ Failed to fetch commit${NC}"
            echo
            continue
        fi

        echo "  Commit: ${commit:0:7} → ${latest:0:7}"

        if [[ "$commit" != "$latest" ]]; then
            echo -e "  ${GREEN}✨ Updating snapshot commit${NC}"

            update_git_snapshot "$spec" "$latest"

            UPDATED=$((UPDATED + 1))
        else
            echo "  ℹ Up to date"
        fi

        if is_rust_package "$spec"; then
            generate_cargo_vendor "$dir" "$latest" "$url" || true
        fi

        echo
        continue
    fi

    # --------------------------------------------------
    # Stable releases
    # --------------------------------------------------

    if [[ "$pkg" == "postman" ]]; then
        latest="$(get_postman_version || true)"
    else
        latest="$(get_latest_tag "$url" || true)"
    fi

    if [[ -z "$latest" ]]; then
        echo -e "  ${RED}⚠ Failed to fetch latest version${NC}"
        echo
        continue
    fi

    echo "  Latest: $latest"

    if [[ "$version" != "$latest" ]]; then
        echo -e "  ${GREEN}✨ Updating: $version → $latest${NC}"

        update_version "$spec" "$latest"

        UPDATED=$((UPDATED + 1))

        version="$latest"
    else
        echo "  ℹ Up to date"
    fi

    if is_rust_package "$spec"; then
        generate_cargo_vendor "$dir" "$version" "$url" || true
    fi

    echo
done

# --------------------------------------------------
# Summary
# --------------------------------------------------

if [[ "$UPDATED" -gt 0 ]]; then
    echo -e "${GREEN}✅ Done! Updated $UPDATED target(s).${NC}"
    echo "Run: git status"
else
    echo -e "${GREEN}✅ Everything is already up to date.${NC}"
fi