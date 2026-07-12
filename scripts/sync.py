#!/usr/bin/env python3
import os
import sys
import re
import json
import shutil
import subprocess
import tempfile
import difflib
from urllib.request import Request, urlparse, urlopen
from urllib.error import URLError
from concurrent.futures import ThreadPoolExecutor

TIMEOUT = 15
GREEN = '\033[0;32m'
YELLOW = '\033[1;33m'
BLUE = '\033[0;34m'
RED = '\033[0;31m'
NC = '\033[0m'

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def file_name_auto_patch(name: str) -> str:
    return f"{name}-fix-metadata-auto.diff"

def get_gh_token():
    if shutil.which("gh"):
        try:
            res = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, check=True)
            token = res.stdout.strip()
            if token:
                return token
        except subprocess.CalledProcessError:
            pass
    return None

def fetch_json(url):
    req = Request(url)
    req.add_header("User-Agent", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36")
    
    if "github.com" in url:
        req.add_header("Accept", "application/vnd.github+json")
        token = get_gh_token()
        if token:
            req.add_header("Authorization", f"Bearer {token}")
    try:
        with urlopen(req, timeout=TIMEOUT) as response:
            return json.loads(response.read().decode())
    except Exception as e:
        print(f"  {RED}⚠ Error fetching JSON from {url}: {e}{NC}", file=sys.stderr)
        return None

def download_file(url, dest_path):
    req = Request(url)
    token = get_gh_token()
    if token and "github.com" in url:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urlopen(req, timeout=TIMEOUT) as response, open(dest_path, "wb") as out_file:
            shutil.copyfileobj(response, out_file)
        return True
    except URLError:
        return False

def github_repo_path(url):
    return url.replace("https://github.com/", "").strip("/")

def get_latest_commit(url):
    repo = github_repo_path(url)
    data = fetch_json(f"https://api.github.com/repos/{repo}/commits/HEAD")
    if data and isinstance(data, dict):
        return data.get("sha")
    return None

def get_latest_tag(url):
    repo = github_repo_path(url)
    
    data = fetch_json(f"https://api.github.com/repos/{repo}/releases/latest")
    if data and isinstance(data, dict) and "tag_name" in data:
        return sanitize_rpm_version(data["tag_name"])
        
    tags_data = fetch_json(f"https://api.github.com/repos/{repo}/tags")
    if tags_data and isinstance(tags_data, list) and len(tags_data) > 0:
        return sanitize_rpm_version(tags_data[0].get("name"))
        
    return "1.0.0"

def get_postman_version():
    data = fetch_json("https://www.postman.com/mkapi/release.json")
    if data and "notes" in data and len(data["notes"]) > 0:
        return sanitize_rpm_version(data["notes"][0].get("version", "1.0.0"))
    return "1.0.0"

def sanitize_rpm_version(version):
    if not version:
        return "1.0.0"
    version = version.replace("-", ".").replace("_", ".")
    if version.startswith("v"):
        version = version[1:]
    return version

def parse_spec(spec_path):
    version, url, commit = None, None, None
    with open(spec_path, "r", encoding="utf-8") as f:
        content = f.read()

    v_match = re.search(r"^%global\s+version\s+(\S+)", content, re.MULTILINE)
    if v_match:
        version = v_match.group(1)
    else:
        v_match = re.search(r"^Version:\s*(\S+)", content, re.MULTILINE)
        if v_match:
            version = v_match.group(1)

    u_match = re.search(r"^%global\s+forgeurl\s+(\S+)", content, re.MULTILINE)
    if u_match:
        url = u_match.group(1)
    else:
        u_match = re.search(r"^URL:\s*(\S+)", content, re.MULTILINE)
        if u_match:
            url = u_match.group(1)

    c_match = re.search(r"^%global\s+commit\s+(\S+)", content, re.MULTILINE)
    if c_match:
        commit = c_match.group(1)

    is_snapshot = "%global commit" in content
    is_rust = bool(re.search(r"cargo|rust", content, re.IGNORECASE))

    return version, url, commit, is_snapshot, is_rust

def update_spec_file(spec_path, key, new_value):
    with open(spec_path, "r", encoding="utf-8") as f:
        content = f.read()

    if key == "version":
        if re.search(r"^%global\s+version\s+", content, re.MULTILINE):
            content = re.sub(r"^%global\s+version\s+.*", f"%global version {new_value}", content, flags=re.MULTILINE)
        else:
            content = re.sub(r"^Version:\s*.*", f"Version:        {new_value}", content, flags=re.MULTILINE)
    elif key == "commit":
        content = re.sub(r"^%global\s+commit\s+.*", f"%global commit   {new_value}", content, flags=re.MULTILINE)

    with open(spec_path, "w", encoding="utf-8") as f:
        f.write(content)

def inject_patch_into_spec(spec_path, pkg_name):
    with open(spec_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    patch_filename = file_name_auto_patch(pkg_name)
    patch_line = f"Patch0:         {patch_filename}\n"
    
    has_patch = any(re.match(r"^Patch0:\s*", line) for line in lines)
    if has_patch:
        return False

    last_source_idx = -1
    for idx, line in enumerate(lines):
        if re.match(r"^Source\d*:\s*", line):
            last_source_idx = idx

    if last_source_idx != -1:
        lines.insert(last_source_idx + 1, patch_line)
        with open(spec_path, "w", encoding="utf-8") as f:
            f.writelines(lines)
        return True
    
    return False

def preprocess_cargo_toml_helper(contents: str) -> str | None:
    try:
        ret1 = subprocess.run(
            ["rust2rpm-helper", "normalize-version", "-"],
            input=contents,
            text=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        patched1 = ret1.stdout or contents

        ret2 = subprocess.run(
            ["rust2rpm-helper", "strip-foreign", "-"],
            input=patched1,
            text=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        patched2 = ret2.stdout or patched1

        if patched2 == contents:
            return None

        return patched2
    except subprocess.CalledProcessError as e:
        print(f"  {RED}⚠ rust2rpm-helper processing failed: {e.stderr.strip()}{NC}")
        return None

def generate_cargo_vendor(pkg_dir, target_ref, url, spec_path):
    pkg_name = os.path.basename(pkg_dir)
    vendor_tarball = os.path.join(pkg_dir, "vendor.tar.gz")
    patch_file = os.path.join(pkg_dir, file_name_auto_patch(pkg_name))

    if os.path.exists(vendor_tarball):
        return 0

    if not shutil.which("cargo"):
        print(f"  {RED}⚠ cargo not found for {pkg_name}{NC}")
        return 0

    if not shutil.which("rust2rpm-helper"):
        print(f"  {RED}⚠ rust2rpm-helper not found in $PATH! Skipping metadata patch generation for {pkg_name}{NC}")
        return 0

    print(f"  {BLUE}📦 Downloading upstream tarball for {pkg_name}...{NC}")
    tmp_dir = tempfile.mkdtemp()
    tarball_path = os.path.join(tmp_dir, "source.tar.gz")
    repo = github_repo_path(url)
    tarball_url = f"https://api.github.com/repos/{repo}/tarball/{target_ref}"

    try:
        if not download_file(tarball_url, tarball_path):
            print(f"  {RED}⚠ Failed to download tarball for {pkg_name}{NC}")
            return 0

        extract_dir = os.path.join(tmp_dir, "extract")
        os.makedirs(extract_dir, exist_ok=True)
        
        res = subprocess.run(["tar", "-xzf", tarball_path, "-C", extract_dir], capture_output=True)
        if res.returncode != 0:
            print(f"  {RED}⚠ Failed to extract tarball for {pkg_name}{NC}")
            return 0

        subdirs = os.listdir(extract_dir)
        if not subdirs:
            return 0
        src_dir = os.path.join(extract_dir, subdirs[0])

        cargo_toml = os.path.join(src_dir, "Cargo.toml")
        updated_count = 0

        if os.path.exists(cargo_toml):
            with open(cargo_toml, "r", encoding="utf-8") as f:
                original_contents = f.read()

            patched_contents = preprocess_cargo_toml_helper(original_contents)
            
            if patched_contents:
                print(f"  {GREEN}✨ Non-Linux targets stripped by rust2rpm-helper. Generating patch for {pkg_name}...{NC}")
                
                with open(cargo_toml, "w", encoding="utf-8") as f:
                    f.write(patched_contents)

                diff = difflib.unified_diff(
                    original_contents.splitlines(keepends=True),
                    patched_contents.splitlines(keepends=True),
                    fromfile="a/Cargo.toml", tofile="b/Cargo.toml"
                )
                with open(patch_file, "w", encoding="utf-8") as pf:
                    pf.writelines(diff)
                updated_count += 1

                if inject_patch_into_spec(spec_path, pkg_name):
                    print(f"  {GREEN}✨ Patch0 successfully added to {pkg_name}.spec{NC}")
                    updated_count += 1
            else:
                if os.path.exists(patch_file):
                    os.remove(patch_file)

        vendor_out_dir = os.path.join(tmp_dir, "vendor")
        vendor_res = subprocess.run(["cargo", "vendor", vendor_out_dir], cwd=src_dir, capture_output=True, text=True)
        
        if vendor_res.returncode == 0:
            subprocess.run(["tar", "-czf", vendor_tarball, "-C", tmp_dir, "vendor"], check=True)
            print(f"  {GREEN}✨ vendor.tar.gz created for {pkg_name}!{NC}")
            updated_count += 1
            return updated_count
        else:
            print(f"  {RED}⚠ cargo vendor execution failed for {pkg_name}{NC}")
            return 0

    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)

def process_package(item):
    dir_path = os.path.join(REPO_ROOT, item)
    spec_path = os.path.join(dir_path, f"{item}.spec")
    if not os.path.exists(spec_path):
        return 0

    print(f"{YELLOW}Checking package: {item}...{NC}")
    current_version, url, current_commit, is_snapshot, is_rust = parse_spec(spec_path)
    
    local_updates = 0
    latest_tag = get_postman_version() if item == "postman" else get_latest_tag(url)

    if is_snapshot:
        latest_commit = get_latest_commit(url)
        if not latest_commit:
            print(f"  {RED}⚠ Failed to fetch upstream commit metadata for {item}{NC}\n")
            return 0

        if current_version != latest_tag:
            update_spec_file(spec_path, "version", latest_tag)
            local_updates += 1
            current_version = latest_tag

        if current_commit != latest_commit:
            print(f"  {GREEN}✨ Updating snapshot commit for {item}{NC}")
            update_spec_file(spec_path, "commit", latest_commit)
            local_updates += 1
            if is_rust:
                auto_patch = file_name_auto_patch(item)
                for f_remove in ["vendor.tar.gz", auto_patch, f"{item}-cargo.diff", f"{item}-remove-non-linux-deps.patch"]:
                    p = os.path.join(dir_path, f_remove)
                    if os.path.exists(p):
                        os.remove(p)
        
        if is_rust:
            local_updates += generate_cargo_vendor(dir_path, latest_commit, url, spec_path)
        return local_updates

    if current_version != latest_tag:
        print(f"  {GREEN}✨ Updating version for {item}: {current_version} → {latest_tag}{NC}")
        update_spec_file(spec_path, "version", latest_tag)
        local_updates += 1
        if is_rust:
            auto_patch = file_name_auto_patch(item)
            for f_remove in ["vendor.tar.gz", auto_patch, f"{item}-cargo.diff", f"{item}-remove-non-linux-deps.patch"]:
                p = os.path.join(dir_path, f_remove)
                if os.path.exists(p):
                    os.remove(p)
        current_version = latest_tag

    if is_rust:
        local_updates += generate_cargo_vendor(dir_path, current_version, url, spec_path)

    return local_updates

def main():
    print(f"{BLUE}🔍 Syncing package versions with automated patch naming and Spec integration...{NC}\n")
    
    if not os.path.exists(REPO_ROOT):
        sys.exit(1)

    packages = [
        item for item in os.listdir(REPO_ROOT)
        if os.path.isdir(os.path.join(REPO_ROOT, item)) and item not in [".git", "scripts", ".github"]
    ]

    total_updated = 0
    with ThreadPoolExecutor() as executor:
        results = executor.map(process_package, packages)
        total_updated = sum(results)

    print("\n--------------------------------------------------")
    if total_updated > 0:
        print(f"{GREEN}✅ Done! Successfully updated {total_updated} target(s)/asset(s).{NC}")
        print("Check updates: git status")
    else:
        print(f"{GREEN}✅ All packages are up to date with the latest versions.{NC}")

if __name__ == "__main__":
    main()