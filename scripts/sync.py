#!/usr/bin/env python3
import os
import sys
import re
import json
import shutil
import subprocess
from datetime import datetime
from urllib.request import Request, urlopen
from concurrent.futures import ThreadPoolExecutor

TIMEOUT = 15
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Terminal Colors
GREEN, YELLOW, RED, BOLD, NC = "\033[0;32m", "\033[1;33m", "\033[0;31m", "\033[1m", "\033[0m"


def fetch_json(url, is_crates_io=False):
    req = Request(url)
    if is_crates_io:
        req.add_header("User-Agent", "RPM-Package-Sync (contact@example.com)")
    else:
        req.add_header("User-Agent", "Mozilla/5.0 (X11; Linux x86_64)")
        if "github.com" in url:
            req.add_header("Accept", "application/vnd.github+json")
            token = os.getenv("GH_TOKEN") or get_gh_token()
            if token:
                req.add_header("Authorization", f"Bearer {token}")
    try:
        with urlopen(req, timeout=TIMEOUT) as resp:
            return json.loads(resp.read().decode())
    except Exception:
        return None


def get_gh_token():
    if shutil.which("gh"):
        try:
            res = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, check=True)
            return res.stdout.strip()
        except subprocess.CalledProcessError:
            pass
    return None


def get_upstream_version(item, url, is_snapshot):
    if is_snapshot:
        repo = url.replace("https://github.com/", "").strip("/")
        data = fetch_json(f"https://api.github.com/repos/{repo}/commits/HEAD")
        if data and isinstance(data, dict):
            sha = data.get("sha")
            date_str = data.get("commit", {}).get("committer", {}).get("date", "")
            date = datetime.strptime(date_str[:10], "%Y-%m-%d").strftime("%Y%m%d")
            return f"0^{date}.g{sha[:7]}", sha
        return None, None

    if item.startswith("rust-"):
        crate_name = item[5:]
        data = fetch_json(f"https://crates.io/api/v1/crates/{crate_name}", is_crates_io=True)
        tag = data.get("crate", {}).get("max_version", "1.0.0") if data else "1.0.0"
    elif item == "postman":
        data = fetch_json("https://www.postman.com/mkapi/release.json")
        tag = data["notes"][0].get("version", "1.0.0") if data and "notes" in data and data["notes"] else "1.0.0"
    else:
        repo = url.replace("https://github.com/", "").strip("/")
        data = fetch_json(f"https://api.github.com/repos/{repo}/releases/latest")
        tag = data.get("tag_name", "1.0.0") if data and isinstance(data, dict) else "1.0.0"

    clean_ver = tag.lstrip("v").replace("-", ".").replace("_", ".")
    return clean_ver, None


def parse_spec(spec_path):
    with open(spec_path, "r", encoding="utf-8") as f:
        content = f.read()

    v_match = re.search(r"^(?:%global\s+version|Version:)\s+(\S+)", content, re.MULTILINE)
    u_match = re.search(r"^URL:\s*(\S+)", content, re.MULTILINE)
    c_match = re.search(r"^%global\s+commit\s+(\S+)", content, re.MULTILINE)
    crate_match = re.search(r"^%global\s+crate\s+(\S+)", content, re.MULTILINE)

    version = v_match.group(1) if v_match else None
    url = u_match.group(1) if u_match else None
    commit = c_match.group(1) if c_match else None
    crate_val = crate_match.group(1) if crate_match else None

    return {
        "version": version,
        "url": url,
        "commit": commit,
        "crate": crate_val,
        "is_snapshot": "%global commit" in content,
        "is_rust": bool(re.search(r"cargo|rust", content, re.IGNORECASE)),
    }


def update_spec_file(spec_path, key, value):
    with open(spec_path, "r", encoding="utf-8") as f:
        content = f.read()

    if key == "version":
        pattern = r"^%global\s+version\s+.*" if "%global version" in content else r"^Version:\s*.*"
        replacement = f"%global version {value}" if "%global version" in content else f"Version:        {value}"
    elif key == "commit":
        pattern, replacement = r"^%global\s+commit\s+.*", f"%global commit {value}"

    content = re.sub(pattern, replacement, content, flags=re.MULTILINE)
    with open(spec_path, "w", encoding="utf-8") as f:
        f.write(content)


def run_rust2rpm(pkg_dir, pkg_name, crate_val, spec_path):
    if not shutil.which("rust2rpm"):
        return 0

    target = crate_val or (pkg_name[5:] if pkg_name.startswith("rust-") else pkg_name)
    toml_path = os.path.join(pkg_dir, "rust2rpm.toml")
    cmd = ["rust2rpm", "-a", "-V", "auto", target, "-o", pkg_dir] + (["-C", toml_path] if os.path.exists(toml_path) else [])

    # Preserve dynamic license block if present
    license_block = None
    if os.path.exists(spec_path):
        with open(spec_path, "r", encoding="utf-8") as f:
            match = re.search(r"(%package\s+-n\s+%{crate}.*?# LICENSE\.dependencies contains a full license breakdown)", f.read(), re.DOTALL)
            if match:
                license_block = match.group(1).strip()

    try:
        subprocess.run(cmd, capture_output=True, text=True, check=True)
        if license_block and os.path.exists(spec_path):
            with open(spec_path, "r+", encoding="utf-8") as f:
                content = f.read()
                f.seek(0)
                f.write(re.sub(r"(%package\s+-n\s+%{crate}.*?# LICENSE\.dependencies contains a full license breakdown)", license_block, content, flags=re.DOTALL))
                f.truncate()
        return 1
    except subprocess.CalledProcessError:
        return 0


def process_package(item):
    dir_path = os.path.join(REPO_ROOT, item)
    spec_path = os.path.join(dir_path, f"{item}.spec")

    if not os.path.exists(spec_path):
        return {"name": item, "status": "No Spec", "updates": 0, "version": "-"}

    meta = parse_spec(spec_path)
    latest_ver, latest_commit = get_upstream_version(item, meta["url"], meta["is_snapshot"])

    if not latest_ver:
        return {"name": item, "status": "Failed API", "updates": 0, "version": meta["version"]}

    updates = 0
    status = "Up to date"

    if meta["version"] != latest_ver or (meta["is_snapshot"] and meta["commit"] != latest_commit):
        update_spec_file(spec_path, "version", latest_ver)
        if meta["is_snapshot"]:
            update_spec_file(spec_path, "commit", latest_commit)
        updates += 1
        status = f"Updated ({latest_ver})"

    if meta["is_rust"]:
        r_updates = run_rust2rpm(dir_path, item, meta["crate"], spec_path)
        updates += r_updates
        if r_updates > 0 and status == "Up to date":
            status = "Rust2rpm Re-generated"

    return {"name": item, "status": status, "updates": updates, "version": latest_ver}


def main():
    if not os.path.exists(REPO_ROOT):
        sys.exit(1)

    packages = sorted([
        d for d in os.listdir(REPO_ROOT)
        if os.path.isdir(os.path.join(REPO_ROOT, d)) and d not in [".git", "scripts", ".github"]
    ])
    max_len = max([len(p) for p in packages], default=20)

    print(f"{BOLD}🔍 Syncing package versions...{NC}\n")

    with ThreadPoolExecutor() as executor:
        results = list(executor.map(process_package, packages))

    print(f"\n{BOLD}{'PACKAGE':<{max_len + 2}} {'VERSION':<18} {'STATUS'}{NC}")
    print("-" * (max_len + 40))

    total_updated = 0
    for res in results:
        total_updated += res["updates"]
        color = GREEN if "Up to date" in res["status"] else (RED if "Failed" in res["status"] or "No Spec" in res["status"] else YELLOW)
        print(f"  {res['name']:<{max_len}} {res['version']:<18} {color}{res['status']}{NC}")

    print("\n" + "=" * (max_len + 40))
    if total_updated > 0:
        print(f"{GREEN}{BOLD}✅ Finished! Updated {total_updated} package(s).{NC}")
    else:
        print(f"{GREEN}{BOLD}✅ All packages are up to date.{NC}")


if __name__ == "__main__":
    main()