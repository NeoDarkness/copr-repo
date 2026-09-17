#!/usr/bin/env python3

import json
import os
import re
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from urllib.request import Request, urlopen

TIMEOUT = 15
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Terminal Colors & Indicators
GREEN, YELLOW, RED, BLUE, BOLD, NC = (
    "\033[0;32m",
    "\033[1;33m",
    "\033[0;31m",
    "\033[0;34m",
    "\033[1m",
    "\033[0m",
)


def log_verbose(pkg_name, message, level="INFO"):
    """Helper to print formatted verbose logs."""
    color = BLUE if level == "INFO" else (YELLOW if level == "WARN" else RED)
    print(f"[{color}{level:<4}{NC}] [{BOLD}{pkg_name:<15}{NC}] {message}")


def get_gh_token():
    if shutil.which("gh"):
        try:
            res = subprocess.run(
                ["gh", "auth", "token"],
                capture_output=True,
                text=True,
                check=True,
            )
            return res.stdout.strip()
        except subprocess.CalledProcessError:
            pass

    return None


def fetch_json(url, item="SYSTEM", is_crates_io=False):
    log_verbose(item, f"Fetching API: {url}")
    req = Request(url)

    if is_crates_io:
        req.add_header(
            "User-Agent",
            "RPM-Package-Sync (contact@example.com)",
        )
    else:
        req.add_header(
            "User-Agent",
            "Mozilla/5.0 (X11; Linux x86_64)",
        )

        if "github.com" in url:
            req.add_header(
                "Accept",
                "application/vnd.github+json",
            )

            token = os.getenv("GH_TOKEN") or get_gh_token()

            if token:
                req.add_header(
                    "Authorization",
                    f"Bearer {token}",
                )

    try:
        with urlopen(req, timeout=TIMEOUT) as resp:
            return json.loads(resp.read().decode())
    except Exception as e:
        log_verbose(item, f"HTTP/API Error on {url}: {e}", level="WARN")
        return None


def get_upstream_version(item, url, is_snapshot):
    if is_snapshot:
        repo = url.replace(
            "https://github.com/",
            "",
        ).strip("/")

        log_verbose(item, f"Fetching snapshot commit data from GitHub: {repo}")
        data = fetch_json(
            f"https://api.github.com/repos/{repo}/commits/HEAD", item=item
        )

        if data and isinstance(data, dict):
            sha = data.get("sha")
            date_str = data.get("commit", {}).get("committer", {}).get("date", "")

            if not sha or not date_str:
                log_verbose(
                    item,
                    "Failed to retrieve SHA or Date from GitHub response",
                    level="WARN",
                )
                return None, None, None

            try:
                date = datetime.strptime(
                    date_str[:10],
                    "%Y-%m-%d",
                ).strftime("%Y%m%d")
            except ValueError:
                log_verbose(
                    item, f"Failed to parse date format: {date_str}", level="WARN"
                )
                return None, None, None

            version = f"0^{date}git.{sha[:7]}"
            log_verbose(item, f"Found upstream snapshot version: {version}")
            return version, sha, date

        return None, None, None

    if item.startswith("rust-"):
        crate_name = item[5:]
        log_verbose(item, f"Fetching latest version from Crates.io: {crate_name}")

        data = fetch_json(
            f"https://crates.io/api/v1/crates/{crate_name}",
            item=item,
            is_crates_io=True,
        )

        tag = data.get("crate", {}).get("max_version", "1.0.0") if data else "1.0.0"

    elif item == "postman":
        log_verbose(item, "Fetching latest version from Postman API")
        data = fetch_json("https://www.postman.com/mkapi/release.json", item=item)

        tag = (
            data["notes"][0].get("version", "1.0.0")
            if data and "notes" in data and data["notes"]
            else "1.0.0"
        )

    else:
        repo = url.replace(
            "https://github.com/",
            "",
        ).strip("/")

        log_verbose(item, f"Fetching latest release from GitHub: {repo}")
        data = fetch_json(
            f"https://api.github.com/repos/{repo}/releases/latest", item=item
        )

        tag = (
            data.get("tag_name", "1.0.0")
            if data and isinstance(data, dict)
            else "1.0.0"
        )

    clean_ver = tag.lstrip("v").replace("-", ".").replace("_", ".")
    log_verbose(item, f"Found upstream release version: {clean_ver}")

    return clean_ver, None, None


def parse_spec(spec_path):
    with open(spec_path, "r", encoding="utf-8") as f:
        content = f.read()

    v_match = re.search(
        r"^(?:%global\s+version|Version:)\s+(\S+)",
        content,
        re.MULTILINE,
    )

    u_match = re.search(
        r"^URL:\s*(\S+)",
        content,
        re.MULTILINE,
    )

    c_match = re.search(
        r"^%global\s+commit\s+(\S+)",
        content,
        re.MULTILINE,
    )

    cd_match = re.search(
        r"^%global\s+commitdate\s+(\S+)",
        content,
        re.MULTILINE,
    )

    crate_match = re.search(
        r"^%global\s+crate\s+(\S+)",
        content,
        re.MULTILINE,
    )

    version = v_match.group(1) if v_match else None
    url = u_match.group(1) if u_match else None
    commit = c_match.group(1) if c_match else None
    commitdate = cd_match.group(1) if cd_match else None
    crate_val = crate_match.group(1) if crate_match else None

    return {
        "version": version,
        "url": url,
        "commit": commit,
        "commitdate": commitdate,
        "crate": crate_val,
        "is_snapshot": "%global commit" in content,
        "is_rust": bool(
            re.search(
                r"cargo|rust",
                content,
                re.IGNORECASE,
            )
        ),
    }


def update_spec_file(spec_path, key, value, item):
    log_verbose(item, f"Updating .spec file -> Changing {key} to '{value}'")
    with open(spec_path, "r", encoding="utf-8") as f:
        content = f.read()

    if key == "version":
        if "%global version" in content:
            pattern = r"^%global\s+version\s+.*$"
            replacement = f"%global version {value}"
        else:
            pattern = r"^Version:\s*.*$"
            replacement = f"Version:        {value}"

    elif key == "commit":
        pattern = r"^%global\s+commit\s+.*$"
        replacement = f"%global commit {value}"

    elif key == "commitdate":
        pattern = r"^%global\s+commitdate\s+.*$"
        replacement = f"%global commitdate {value}"

    else:
        return

    content = re.sub(
        pattern,
        replacement,
        content,
        flags=re.MULTILINE,
    )

    with open(spec_path, "w", encoding="utf-8") as f:
        f.write(content)


def run_rust2rpm(pkg_dir, pkg_name, crate_val, spec_path):
    if not shutil.which("rust2rpm"):
        log_verbose(pkg_name, "rust2rpm not found in system (skipping)", level="WARN")
        return False

    target = crate_val or (pkg_name[5:] if pkg_name.startswith("rust-") else pkg_name)
    toml_path = os.path.join(pkg_dir, "rust2rpm.toml")

    cmd = ["rust2rpm", "-a", "-V", "auto", target, "-o", pkg_dir]

    if os.path.exists(toml_path):
        cmd += ["-C", toml_path]

    log_verbose(pkg_name, f"Executing rust2rpm: {' '.join(cmd)}")

    license_block = None
    if os.path.exists(spec_path):
        with open(spec_path, "r", encoding="utf-8") as f:
            match = re.search(
                r"(%package\s+-n\s+%{crate}.*?# LICENSE\.dependencies contains a full license breakdown)",
                f.read(),
                re.DOTALL,
            )
            if match:
                license_block = match.group(1).strip()

    # Pass Git identity variables directly to rust2rpm process as fallback
    env = os.environ.copy()
    env["GIT_AUTHOR_NAME"] = env.get("GIT_AUTHOR_NAME", "github-actions[bot]")
    env["GIT_AUTHOR_EMAIL"] = env.get(
        "GIT_AUTHOR_EMAIL", "41898282+github-actions[bot]@users.noreply.github.com"
    )
    env["GIT_COMMITTER_NAME"] = env.get("GIT_COMMITTER_NAME", "github-actions[bot]")
    env["GIT_COMMITTER_EMAIL"] = env.get(
        "GIT_COMMITTER_EMAIL", "41898282+github-actions[bot]@users.noreply.github.com"
    )

    try:
        subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True,
            env=env,
        )

        if license_block and os.path.exists(spec_path):
            log_verbose(pkg_name, "Restoring custom license block in .spec file")
            with open(spec_path, "r+", encoding="utf-8") as f:
                content = f.read()

                content = re.sub(
                    r"(%package\s+-n\s+%{crate}.*?# LICENSE\.dependencies contains a full license breakdown)",
                    license_block,
                    content,
                    flags=re.DOTALL,
                )

                f.seek(0)
                f.write(content)
                f.truncate()

        log_verbose(pkg_name, "Successfully regenerated Rust spec file")
        return True

    except subprocess.CalledProcessError as e:
        err_msg = e.stderr.strip() if e.stderr else str(e)
        log_verbose(
            pkg_name,
            f"rust2rpm execution failed:\n{err_msg}",
            level="WARN",
        )
        return False


def process_package(item):
    log_verbose(item, "Starting package processing...")
    dir_path = os.path.join(REPO_ROOT, item)
    spec_path = os.path.join(dir_path, f"{item}.spec")

    if not os.path.exists(spec_path):
        log_verbose(item, ".spec file not found!", level="WARN")
        return {
            "name": item,
            "status": "No Spec",
            "updates": 0,
            "version": "-",
            "failed": True,
        }

    meta = parse_spec(spec_path)
    log_verbose(
        item,
        f"Local Spec details -> Version: {meta['version']}, Snapshot: {meta['is_snapshot']}, Rust: {meta['is_rust']}",
    )

    if not meta["url"]:
        log_verbose(item, "URL not found in .spec file!", level="WARN")
        return {
            "name": item,
            "status": "No URL",
            "updates": 0,
            "version": meta["version"] or "-",
            "failed": True,
        }

    latest_ver, latest_commit, latest_date = get_upstream_version(
        item,
        meta["url"],
        meta["is_snapshot"],
    )

    if not latest_ver:
        log_verbose(item, "Failed to retrieve upstream version data", level="WARN")
        return {
            "name": item,
            "status": "Failed API",
            "updates": 0,
            "version": meta["version"],
            "failed": True,
        }

    updates = 0
    status = "Up to date"
    failed = False

    if meta["is_snapshot"]:
        commit_changed = meta["commit"] != latest_commit
        date_changed = meta["commitdate"] != latest_date

        if commit_changed or date_changed:
            if commit_changed:
                log_verbose(
                    item, f"Commit changed ({meta['commit']} -> {latest_commit})"
                )
                update_spec_file(spec_path, "commit", latest_commit, item)

            if date_changed:
                log_verbose(
                    item, f"Commitdate changed ({meta['commitdate']} -> {latest_date})"
                )
                update_spec_file(spec_path, "commitdate", latest_date, item)

            updates += 1
            status = f"Updated ({latest_date}git.{latest_commit[:7]})"

    else:
        if meta["version"] != latest_ver:
            log_verbose(item, f"Version changed ({meta['version']} -> {latest_ver})")
            update_spec_file(spec_path, "version", latest_ver, item)
            updates += 1
            status = f"Updated ({latest_ver})"

    if meta["is_rust"]:
        rust_success = run_rust2rpm(
            dir_path,
            item,
            meta["crate"],
            spec_path,
        )

        if rust_success:
            updates += 1
            if status == "Up to date":
                status = "Rust2rpm Re-generated"
        else:
            failed = True
            if status == "Up to date":
                status = "Rust2rpm Failed"

    log_verbose(item, f"Processing complete. Final status: {status}")
    return {
        "name": item,
        "status": status,
        "updates": updates,
        "version": latest_ver,
        "failed": failed,
    }


def main():
    if not os.path.exists(REPO_ROOT):
        sys.exit(1)

    packages = sorted(
        [
            d
            for d in os.listdir(REPO_ROOT)
            if os.path.isdir(os.path.join(REPO_ROOT, d))
            and d
            not in [
                ".git",
                "scripts",
                ".github",
            ]
        ]
    )

    max_len = max(
        [len(p) for p in packages],
        default=20,
    )

    print(f"{BOLD}🔍 Syncing package versions (Verbose Mode Enabled)...{NC}\n")

    with ThreadPoolExecutor() as executor:
        results = list(
            executor.map(
                process_package,
                packages,
            )
        )

    print(
        f"\n{BOLD}"
        f"{'PACKAGE':<{max_len + 2}} "
        f"{'VERSION':<30} "
        f"{'STATUS'}"
        f"{NC}"
    )

    print("-" * (max_len + 52))

    total_updated = 0
    total_failed = 0

    for res in results:
        total_updated += res["updates"]
        if res.get("failed"):
            total_failed += 1

        color = (
            GREEN
            if "Up to date" in res["status"] or "Re-generated" in res["status"]
            else (
                RED
                if (
                    "Failed" in res["status"]
                    or "No Spec" in res["status"]
                    or "No URL" in res["status"]
                )
                else YELLOW
            )
        )

        print(
            f"  {res['name']:<{max_len}} "
            f"{res['version']:<30} "
            f"{color}{res['status']}{NC}"
        )

    print("\n" + "=" * (max_len + 52))

    if total_failed > 0:
        print(
            f"{RED}{BOLD}❌ Finished with errors! {total_failed} package(s) failed.{NC}"
        )
        sys.exit(1)
    elif total_updated > 0:
        print(
            f"{GREEN}{BOLD}✅ Finished! Updated/regenerated {total_updated} package(s).{NC}"
        )
    else:
        print(f"{GREEN}{BOLD}✅ All packages are up to date.{NC}")


if __name__ == "__main__":
    main()
