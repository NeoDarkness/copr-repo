#!/usr/bin/env python3
import os
import sys
import re
import json
import shutil
import subprocess
import threading
from datetime import datetime
from urllib.request import Request, urlopen
from urllib.error import URLError
from concurrent.futures import ThreadPoolExecutor

TIMEOUT = 15
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

GREEN = "\033[0;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[0;34m"
CYAN = "\033[0;36m"
RED = "\033[0;31m"
BOLD = "\033[1m"
DIM = "\033[2m"
NC = "\033[0m"

CLEAR_LINE = "\033[2K"
CURSOR_UP = "\033[A"

print_lock = threading.Lock()
active_tasks = {}
task_order = []
max_len = 20


def get_gh_token():
    if shutil.which("gh"):
        try:
            res = subprocess.run(
                ["gh", "auth", "token"], capture_output=True, text=True, check=True
            )
            token = res.stdout.strip()
            if token:
                return token
        except subprocess.CalledProcessError:
            pass
    return None


def fetch_json(url, is_crates_io=False):
    req = Request(url)
    if is_crates_io:
        req.add_header("User-Agent", "RPM-Package-Sync (contact@example.com)")
    else:
        req.add_header("User-Agent", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36")
        if "github.com" in url:
            req.add_header("Accept", "application/vnd.github+json")
            token = get_gh_token()
            if token:
                req.add_header("Authorization", f"Bearer {token}")
    try:
        with urlopen(req, timeout=TIMEOUT) as response:
            return json.loads(response.read().decode())
    except Exception:
        return None


def github_repo_path(url):
    return url.replace("https://github.com/", "").strip("/")


def get_commit_info(url):
    repo = github_repo_path(url)
    data = fetch_json(f"https://api.github.com/repos/{repo}/commits/HEAD")
    if data and isinstance(data, dict):
        sha = data.get("sha")
        date_str = data.get("commit", {}).get("committer", {}).get("date", "")
        datestamp = datetime.strptime(date_str[:10], "%Y-%m-%d").strftime("%Y%m%d")
        return sha, datestamp
    return None, None


def get_latest_tag_raw(url):
    repo = github_repo_path(url)
    data = fetch_json(f"https://api.github.com/repos/{repo}/releases/latest")
    if data and isinstance(data, dict) and "tag_name" in data:
        return data["tag_name"]
    return "1.0.0"


def get_crates_io_version(crate_name):
    clean_name = crate_name[5:] if crate_name.startswith("rust-") else crate_name
    data = fetch_json(f"https://crates.io/api/v1/crates/{clean_name}", is_crates_io=True)
    if data and isinstance(data, dict):
        crate_info = data.get("crate", {})
        max_ver = crate_info.get("max_version")
        if max_ver:
            return max_ver
    return "1.0.0"


def get_postman_version():
    data = fetch_json("https://www.postman.com/mkapi/release.json")
    if data and "notes" in data and len(data["notes"]) > 0:
        return data["notes"][0].get("version", "1.0.0")
    return "1.0.0"


def sanitize_rpm_version(version):
    if not version:
        return "1.0.0"
    version = version.replace("-", ".").replace("_", ".")
    if version.startswith("v"):
        version = version[1:]
    return version


def parse_spec(spec_path):
    version, url, commit, crate_val = None, None, None, None
    with open(spec_path, "r", encoding="utf-8") as f:
        content = f.read()

    v_match = re.search(r"^%global\s+version\s+(\S+)", content, re.MULTILINE)
    if v_match:
        version = v_match.group(1)
    else:
        v_match = re.search(r"^Version:\s*(\S+)", content, re.MULTILINE)
        if v_match:
            version = v_match.group(1)

    forgeurl_match = re.search(r"^%global\s+forgeurl\s+(\S+)", content, re.MULTILINE)
    forgeurl_val = forgeurl_match.group(1) if forgeurl_match else None

    u_match = re.search(r"^URL:\s*(\S+)", content, re.MULTILINE)
    if u_match:
        url = u_match.group(1)
        if url == "%{forgeurl}" and forgeurl_val:
            url = forgeurl_val
    elif forgeurl_val:
        url = forgeurl_val

    c_match = re.search(r"^%global\s+commit\s+(\S+)", content, re.MULTILINE)
    if c_match:
        commit = c_match.group(1)

    crate_match = re.search(r"^%global\s+crate\s+(\S+)", content, re.MULTILINE)
    if crate_match:
        crate_val = crate_match.group(1)

    is_snapshot = "%global commit" in content
    is_rust = bool(re.search(r"cargo|rust", content, re.IGNORECASE))

    return version, url, commit, crate_val, is_snapshot, is_rust


def update_spec_file(spec_path, key, new_value):
    with open(spec_path, "r", encoding="utf-8") as f:
        content = f.read()

    if key == "version":
        if re.search(r"^%global\s+version\s+", content, re.MULTILINE):
            content = re.sub(
                r"^%global\s+version\s+.*",
                f"%global version {new_value}",
                content,
                flags=re.MULTILINE,
            )
        else:
            content = re.sub(
                r"^Version:\s*.*",
                f"Version:        {new_value}",
                content,
                flags=re.MULTILINE,
            )
    elif key == "commit":
        content = re.sub(
            r"^%global\s+commit\s+.*",
            f"%global commit {new_value}",
            content,
            flags=re.MULTILINE,
        )

    with open(spec_path, "w", encoding="utf-8") as f:
        f.write(content)


def update_ui_status(pkg_name, status_text):
    global max_len
    with print_lock:
        active_tasks[pkg_name] = status_text
        if len(task_order) > 0:
            sys.stdout.write(CURSOR_UP * len(task_order))
        for pkg in task_order:
            sys.stdout.write(f"{CLEAR_LINE}  {pkg:<{max_len}} : {active_tasks[pkg]}\n")
        sys.stdout.flush()


def extract_dynamic_license(spec_path):
    if not os.path.exists(spec_path):
        return None
    
    with open(spec_path, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = r"(%package\s+-n\s+%{crate}.*?# LICENSE\.dependencies contains a full license breakdown)"
    match = re.search(pattern, content, re.DOTALL)
    if match:
        return match.group(1).strip()
        
    return None


def run_rust2rpm_command(pkg_dir, pkg_name, crate_val):
    if not shutil.which("rust2rpm"):
        return 0

    spec_path = os.path.join(pkg_dir, f"{pkg_name}.spec")
    dynamic_license = None
    if os.path.exists(spec_path):
        dynamic_license = extract_dynamic_license(spec_path)

    update_ui_status(pkg_name, f"{YELLOW}Running rust2rpm automation...{NC}")
    toml_path = os.path.join(pkg_dir, "rust2rpm.toml")
    
    target_name = crate_val if crate_val else (pkg_name[5:] if pkg_name.startswith("rust-") else pkg_name)
    
    cmd = ["rust2rpm", "-a", "-V", "auto", target_name, "-o", pkg_dir]
    if os.path.exists(toml_path):
        cmd.extend(["-C", toml_path])

    try:
        subprocess.run(cmd, capture_output=True, text=True, check=True)
        
        if dynamic_license and os.path.exists(spec_path):
            with open(spec_path, "r", encoding="utf-8") as f:
                new_content = f.read()
            
            target_pattern = r"(%package\s+-n\s+%{crate}.*?# LICENSE\.dependencies contains a full license breakdown)"
            updated_content, count = re.subn(target_pattern, dynamic_license, new_content, flags=re.DOTALL)
            
            if count > 0:
                with open(spec_path, "w", encoding="utf-8") as f:
                    f.write(updated_content)

        return 1
    except subprocess.CalledProcessError:
        return 0


def process_package(item):
    dir_path = os.path.join(REPO_ROOT, item)
    spec_path = os.path.join(dir_path, f"{item}.spec")
    if not os.path.exists(spec_path):
        update_ui_status(item, f"{RED}Missing .spec file{NC}")
        return {"name": item, "status": "No Spec", "updates": 0, "version": "-"}

    update_ui_status(item, f"{YELLOW}Checking metadata...{NC}")
    current_version, url, current_commit, crate_val, is_snapshot, is_rust = parse_spec(spec_path)

    local_updates = 0
    
    if item.startswith("rust-"):
        raw_tag = get_crates_io_version(item)
    elif item == "postman":
        raw_tag = get_postman_version()
    else:
        raw_tag = get_latest_tag_raw(url)

    if is_snapshot:
        latest_commit, datestamp = get_commit_info(url)
        if not latest_commit:
            update_ui_status(item, f"{RED}API Fetch Failure{NC}")
            return {
                "name": item,
                "status": "Failed API",
                "updates": 0,
                "version": current_version,
            }

        latest_rpm_version = f"0^{datestamp}.g{latest_commit[:7]}"
        status_msg = "Up to date"

        if current_version != latest_rpm_version or current_commit != latest_commit:
            update_spec_file(spec_path, "version", latest_rpm_version)
            update_spec_file(spec_path, "commit", latest_commit)
            local_updates += 1
            status_msg = "Snapshot Updated"
            current_version = latest_rpm_version

        if is_rust:
            local_updates += run_rust2rpm_command(dir_path, item, crate_val)
            if local_updates > 0 and status_msg == "Up to date":
                status_msg = "Rust2rpm Generated"

        update_ui_status(item, f"{GREEN}Finished{NC}")
        return {
            "name": item,
            "status": status_msg,
            "updates": local_updates,
            "version": current_version,
        }

    latest_rpm_version = sanitize_rpm_version(raw_tag)
    status_msg = "Up to date"
    if current_version != latest_rpm_version:
        update_spec_file(spec_path, "version", latest_rpm_version)
        local_updates += 1
        status_msg = f"New Version ({latest_rpm_version})"
        current_version = latest_rpm_version

    if is_rust:
        rust_updates = run_rust2rpm_command(dir_path, item, crate_val)
        local_updates += rust_updates
        if rust_updates > 0 and status_msg == "Up to date":
            status_msg = "Rust2rpm Generated"

    update_ui_status(item, f"{GREEN}Finished{NC}")
    return {
        "name": item,
        "status": status_msg,
        "updates": local_updates,
        "version": current_version,
    }


def main():
    global task_order, max_len
    sys.stdout.write(
        f"{BOLD}{BLUE}🔍 Syncing package versions using optimized parallel runner...{NC}\n\n"
    )
    sys.stdout.flush()

    if not os.path.exists(REPO_ROOT):
        sys.exit(1)
    packages = [
        item
        for item in os.listdir(REPO_ROOT)
        if os.path.isdir(os.path.join(REPO_ROOT, item))
        and item not in [".git", "scripts", ".github"]
    ]
    task_order = sorted(packages)
    max_len = max(len(pkg) for pkg in task_order) if task_order else 20

    for pkg in task_order:
        active_tasks[pkg] = f"{DIM}Pending...{NC}"
        sys.stdout.write(f"  {pkg:<{max_len}} : {active_tasks[pkg]}\n")
    sys.stdout.flush()

    results = []
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(process_package, pkg) for pkg in task_order]
        for future in futures:
            results.append(future.result())

    matrix_width = max(60, max_len + 40)
    sys.stdout.write(f"\n{BOLD}{CYAN}{'=' * matrix_width}{NC}\n")
    sys.stdout.write(
        f"{BOLD}{'PACKAGE':<{max_len + 2}} {'VERSION':<15} {'STATUS':<15} {'CHANGES'}{NC}\n"
    )
    sys.stdout.write(f"{DIM}{'-' * matrix_width}{NC}\n")

    total_updated = 0
    for res in results:
        total_updated += res["updates"]
        status_color = (
            GREEN
            if "Up to date" in res["status"] or "Finished" in res["status"]
            else YELLOW
        )
        if "Failed" in res["status"] or "No Spec" in res["status"]:
            status_color = RED
        sys.stdout.write(
            f"  {res['name']:<{max_len}} {res['version']:<15} {status_color}{res['status']:<15}{NC} {res['updates']}\n"
        )

    sys.stdout.write(f"{BOLD}{CYAN}{'=' * matrix_width}{NC}\n\n")
    if total_updated > 0:
        sys.stdout.write(
            f"{GREEN}{BOLD} ✅ Success! Successfully updated {total_updated} target(s)/asset(s).{NC}\n"
        )
        sys.stdout.write(f"{DIM}Verify local changes with: git status{NC}\n")
    else:
        sys.stdout.write(
            f"{GREEN}{BOLD} ✅ All packages are up to date with upstream tracking.{NC}\n"
        )
    sys.stdout.flush()


if __name__ == "__main__":
    main()