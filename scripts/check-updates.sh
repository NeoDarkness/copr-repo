#!/usr/bin/env bash
# Auto sync RPM spec versions (GitHub + Postman + Forge snapshot commit only)

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

# -------------------------
# HTTP
# -------------------------

github_api() {
    timeout "$TIMEOUT" curl -fsSL \
        -H "Accept: application/vnd.github+json" \
        -H "User-Agent: copr-sync" \
        "$1"
}

# -------------------------
# GitHub helpers
# -------------------------

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

# -------------------------
# Postman
# -------------------------

get_postman_version() {
    timeout "$TIMEOUT" curl -fsSL \
        "https://www.postman.com/mkapi/release.json" \
        | jq -r '.notes[0].version // empty'
}

# -------------------------
# Updaters
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
        "s|^%global[[:space:]]+commit[[:space:]]+.*|%global commit      $commit|" \
        "$spec"
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

        [[ "$commit" == "$latest" ]] && {
            echo "  ℹ️  Up to date"
            continue
        }

        echo -e "  ${GREEN}✨ Updating git snapshot${NC}"
        update_git_snapshot "$spec" "$latest"

        UPDATED=$((UPDATED+1))
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

    [[ "$version" == "$latest" ]] && {
        echo "  ℹ️  Up to date"
        continue
    }

    echo -e "  ${GREEN}✨ Updating: $version → $latest${NC}"
    update_version "$spec" "$latest"

    UPDATED=$((UPDATED+1))
    echo
done

# -------------------------
# Commit
# -------------------------

if [[ "$UPDATED" -gt 0 ]]; then
    cd "$REPO_ROOT"
    git add ./*/*.spec
    git commit -m "chore: sync package versions ($UPDATED)"
    echo -e "${GREEN}✅ Updated $UPDATED package(s)${NC}"
else
    echo -e "${GREEN}✅ No updates needed${NC}"
fi