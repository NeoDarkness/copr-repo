#!/usr/bin/env bash
# Auto sync RPM spec versions (GitHub + Postman + Forge snapshot commit only) + Auto Cargo Vendor

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
UPDATED=0
TIMEOUT=10

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# -------------------------
# Spec helpers
# -------------------------

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
    grep -q "cargo\|rust" "$1"
}

# -------------------------
# HTTP & GitHub helpers
# -------------------------

github_api() {
    timeout "$TIMEOUT" curl -fsSL \
        -H "Accept: application/vnd.github+json" \
        -H "User-Agent: copr-sync" \
        "$1"
}

extract_github_repo() {
    local url="$1"
    url="${url#https://github.com/}"
    url="${url#http://github.com/}"
    url="${url%.git}"
    echo "$url" | cut -d/ -f1-2
}

get_github_version() {
    local repo
    repo=$(extract_github_repo "$1")

    [[ "$repo" =~ .+/.+ ]] || return 1

    github_api "https://api.github.com/repos/$repo/releases/latest" \
        | jq -r '.tag_name // empty' \
        | sed 's/^v//' && return 0

    github_api "https://api.github.com/repos/$repo/tags?per_page=1" \
        | jq -r '.[0].name // empty' \
        | sed 's/^v//'
}

get_github_commit() {
    local repo
    repo=$(extract_github_repo "$1")
    github_api "https://api.github.com/repos/$repo/commits?per_page=1" \
        | jq -r '.[0].sha // empty'
}

get_postman_version() {
    timeout "$TIMEOUT" curl -fsSL \
        "https://www.postman.com/mkapi/release.json" \
        | jq -r '.notes[0].version // empty'
}

# -------------------------
# Updaters & Vendor Generator
# -------------------------

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

generate_cargo_vendor() {
    local pkg_dir="$1"
    local pkg_name="$2"
    local version="$3"
    local url="$4"
    local vendor_tarball="$pkg_dir/vendor.tar.gz"

    # Lewati jika tarball vendor versi ini sudah ada
    if [[ -f "$vendor_tarball" ]]; then
        return 0
    fi

    echo -e "  ${BLUE}📦 Vendor tarball missing. Generating for version $version...${NC}"
    
    # Pastikan perintah cargo tersedia di mesin pelari skrip
    if ! command -v cargo &> /dev/null; then
        echo "  ⚠️  Error: 'cargo' command not found. Cannot generate vendor tarball."
        return 1
    fi

    local repo
    repo=$(extract_github_repo "$url")
    local tmp_dir
    tmp_dir=$(mktemp -d)

    # Hapus file sisa tarball versi lama agar folder bersih
    rm -f "$pkg_dir"/vendor.tar.gz

    # Unduh arsip kode sumber langsung dari GitHub tarball untuk di-vendor
    if timeout "$TIMEOUT" curl -fsSL "https://github.com/$repo/archive/refs/tags/v$version.tar.gz" -o "$tmp_dir/src.tar.gz"; then
        tar -xzf "$tmp_dir/src.tar.gz" -C "$tmp_dir"
        local extracted_dir
        extracted_dir=$(find "$tmp_dir" -maxdepth 1 -type d ! -path "$tmp_dir" | head -n1)

        # Proses pembuatan vendor
        pushd "$extracted_dir" > /dev/null
        if cargo vendor "$tmp_dir/vendor" > /dev/null; then
            tar -czf "$vendor_tarball" -C "$tmp_dir" vendor
            echo -e "  ${GREEN}✨ Vendor tarball created: $(basename "$vendor_tarball")${NC}"
            UPDATED=$((UPDATED+1))
        else
            echo "  ⚠️  Failed running 'cargo vendor'"
        fi
        popd > /dev/null
    else
        echo "  ⚠️  Failed to download source tarball for vendoring"
    fi

    rm -rf "$tmp_dir"
}

# -------------------------
# Main
# -------------------------

echo -e "${BLUE}🔍 Syncing package versions...${NC}\n"

for dir in "$REPO_ROOT"/*; do
    [[ -d "$dir" ]] || continue

    pkg=$(basename "$dir")

    case "$pkg" in
        .git|scripts|.github)
            continue
            ;;
    esac

    spec="$dir/$pkg.spec"
    [[ -f "$spec" ]] || continue

    echo -e "${YELLOW}Checking $pkg...${NC}"

    version=$(get_spec_version "$spec")
    url=$(get_spec_url "$spec")

    echo "  Current: $version"

    # -------------------------
    # Forge snapshot (commit-only)
    # -------------------------
    if is_forge_snapshot "$spec"; then
        commit=$(get_spec_commit "$spec")
        latest=$(get_github_commit "$url" || true)

        [[ -z "$latest" ]] && {
            echo "  ⚠️  Failed to fetch commit"
            continue
        }

        echo "  Commit: ${commit:0:7} → ${latest:0:7}"

        if [[ "$commit" != "$latest" ]]; then
            echo -e "  ${GREEN}✨ Updating git snapshot${NC}"
            update_git_snapshot "$spec" "$latest"
            UPDATED=$((UPDATED+1))
        else
            echo "  ℹ️  Up to date"
        fi
        
        # Pengecekan Vendor khusus ekosistem Rust (Snapshot Version)
        if is_rust_package "$spec"; then
            generate_cargo_vendor "$dir" "$pkg" "$latest" "$url" || true
        fi
        
        echo
        continue
    fi

    # -------------------------
    # Versioned packages (GitHub / Postman)
    # -------------------------
    if [[ "$pkg" == "postman" ]]; then
        latest=$(get_postman_version || true)
    else
        [[ ! "$url" =~ github\.com ]] && {
            echo "  ⚠️  Unsupported source"
            continue
        }

        latest=$(get_github_version "$url" || true)
    fi

    [[ -z "$latest" ]] && {
        echo "  ⚠️  No latest version found"
        continue
    }

    echo "  Latest: $latest"

    if [[ "$version" != "$latest" ]]; then
        echo -e "  ${GREEN}✨ Updating: $version → $latest${NC}"
        update_version "$spec" "$latest"
        UPDATED=$((UPDATED+1))
        version="$latest" # Set variabel lokal ke versi baru untuk keperluan penamaan vendor
    else
        echo "  ℹ️  Up to date"
    fi

    # Pengecekan Vendor khusus ekosistem Rust (Stable Release Version)
    if is_rust_package "$spec"; then
        generate_cargo_vendor "$dir" "$pkg" "$version" "$url" || true
    fi

    echo
done

# -------------------------
# Summary Output Only
# -------------------------
if [[ "$UPDATED" -gt 0 ]]; then
    echo -e "${GREEN}✅ Done! Modified or generated vendor for $UPDATED target(s). Run git status to review changes.${NC}"
else
    echo -e "${GREEN}✅ Everything is already up to date.${NC}"
fi