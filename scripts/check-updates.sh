#!/usr/bin/env bash

# Auto sync RPM spec versions using GitHub API
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
        /^%global[[:space:]]+version[[:space:]]+/ {
            print $3
            found=1
            exit
        }

        /^Version:/ && !found {
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
# GitHub helpers
# --------------------------------------------------

github_repo_path() {
    echo "${1#https://github.com/}"
}

github_api() {
    local url="$1"

    local headers=(
        -H "Accept: application/vnd.github+json"
    )

    if command -v gh >/dev/null 2>&1; then
        local token
        token="$(gh auth token 2>/dev/null || true)"

        if [[ -n "$token" ]]; then
            headers+=(
                -H "Authorization: Bearer $token"
            )
        fi
    fi

    timeout "$TIMEOUT" curl -fsSL \
        "${headers[@]}" \
        "$url"
}

get_latest_commit() {
    local repo
    repo="$(github_repo_path "$1")"

    github_api \
        "https://api.github.com/repos/$repo/commits/HEAD" \
        | jq -r '.sha // empty'
}

get_latest_tag() {
    local repo
    repo="$(github_repo_path "$1")"

    local tags
    tags=$(github_api \
        "https://api.github.com/repos/$repo/tags?per_page=100" \
        | jq -r '.[].name' \
        | sed 's/^v//')

    if [[ -z "$tags" ]]; then
        return
    fi

    local semver_tags
    semver_tags=$(echo "$tags" | grep -E '^[0-9]+\.[0-9]+(\.[0-9]+)?$')

    if [[ -n "$semver_tags" ]]; then
        echo "$semver_tags" | sort -V | tail -n1
    else
        echo "$tags" | sort -V | tail -n1
    fi
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

update_version_macro() {
    local spec="$1"
    local version="$2"

    if grep -q "^%global[[:space:]]\+version[[:space:]]" "$spec"; then
        sed -i -E \
            "s|^%global[[:space:]]+version[[:space:]]+.*|%global version $version|" \
            "$spec"
    else
        sed -i -E \
            "s|^Version:[[:space:]]+.*|Version:        $version|" \
            "$spec"
    fi
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

    if ! git clone \
        --depth 1 \
        --branch "$version" \
        "$url" \
        "$tmp_dir/src" >/dev/null 2>&1; then

        if ! git clone \
            --depth 1 \
            --branch "v$version" \
            "$url" \
            "$tmp_dir/src" >/dev/null 2>&1; then

            echo -e "  ${RED}⚠ git clone failed${NC}"
            rm -rf "$tmp_dir"
            return 1
        fi
    fi

    pushd "$tmp_dir/src" >/dev/null

    if cargo vendor "$tmp_dir/vendor" >/dev/null 2>&1; then
        tar -czf "$vendor_tarball" -C "$tmp_dir" vendor

        echo -e "  ${GREEN}✨ vendor.tar.gz generated${NC}"

        UPDATED=$((UPDATED + 1))
    else
        echo -e "  ${RED}⚠ cargo vendor failed${NC}"
    fi

    popd >/dev/null

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

    echo "  Current: ${version:-snapshot}"

    # --------------------------------------------------
    # Always check latest tag first
    # --------------------------------------------------

    if [[ "$pkg" == "postman" ]]; then
        latest_tag="$(get_postman_version || true)"
    else
        latest_tag="$(get_latest_tag "$url" || true)"
    fi

    if [[ -z "$latest_tag" ]]; then
        latest_tag="1.0.0"
    fi

    # --------------------------------------------------
    # Snapshot packages
    # --------------------------------------------------

    if is_forge_snapshot "$spec"; then
        commit="$(get_spec_commit "$spec")"
        latest_commit="$(get_latest_commit "$url" || true)"

        if [[ -z "$latest_commit" ]]; then
            echo -e "  ${RED}⚠ Failed to fetch commit${NC}"
            echo
            continue
        fi

        echo "  Base Version: $latest_tag"
        echo "  Commit: ${commit:0:7} → ${latest_commit:0:7}"

        if [[ "$version" != "$latest_tag" ]]; then
            echo -e "  ${GREEN}✨ Updating base version${NC}"

            update_version_macro "$spec" "$latest_tag"

            UPDATED=$((UPDATED + 1))
        fi

        if [[ "$commit" != "$latest_commit" ]]; then
            echo -e "  ${GREEN}✨ Updating snapshot commit${NC}"

            update_git_snapshot "$spec" "$latest_commit"

            UPDATED=$((UPDATED + 1))
        else
            echo "  ℹ Snapshot up to date"
        fi

        if is_rust_package "$spec"; then
            generate_cargo_vendor "$dir" "$latest_tag" "$url" || true
        fi

        echo
        continue
    fi

    # --------------------------------------------------
    # Stable releases
    # --------------------------------------------------

    echo "  Latest: $latest_tag"

    if [[ "$version" != "$latest_tag" ]]; then
        echo -e "  ${GREEN}✨ Updating: $version → $latest_tag${NC}"

        update_version_macro "$spec" "$latest_tag"

        UPDATED=$((UPDATED + 1))

        version="$latest_tag"
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