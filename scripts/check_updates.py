#!/usr/bin/env python3

import os
import re
import requests
import yaml
import subprocess
from pathlib import Path
from typing import Dict, Optional, Tuple

# Configuration file path
CONFIG_FILE = Path(__file__).parent.parent / "packages.yml"
REPO_ROOT = Path(__file__).parent.parent

class PackageChecker:
    def __init__(self):
        self.packages = self._load_config()
        self.updated_packages = []

    def _load_config(self) -> Dict:
        """Load package configuration"""
        if not CONFIG_FILE.exists():
            print(f"Config file not found: {CONFIG_FILE}")
            return {}
        
        with open(CONFIG_FILE, 'r') as f:
            return yaml.safe_load(f) or {}

    def check_all_packages(self):
        """Check all packages for updates"""
        print("🔍 Checking for upstream updates...\n")
        
        for package_name, config in self.packages.items():
            print(f"Checking {package_name}...")
            
            if 'source_url' not in config:
                print(f"  ⚠️  No source_url configured, skipping\n")
                continue
            
            current_version = self._get_spec_version(package_name)
            latest_version = self._get_latest_version(config['source_url'], config.get('version_pattern'))
            
            if latest_version and current_version != latest_version:
                print(f"  ✨ New version available: {current_version} → {latest_version}")
                
                if self._update_spec(package_name, latest_version, config):
                    self.updated_packages.append(package_name)
                    print(f"  ✅ Updated successfully\n")
                else:
                    print(f"  ❌ Failed to update\n")
            else:
                print(f"  ℹ️  Already up to date ({current_version})\n")

    def _get_spec_version(self, package_name: str) -> Optional[str]:
        """Extract version from .spec file"""
        spec_file = REPO_ROOT / package_name / f"{package_name}.spec"
        
        if not spec_file.exists():
            return None
        
        with open(spec_file, 'r') as f:
            for line in f:
                match = re.match(r'^Version:\s+(.+)$', line)
                if match:
                    return match.group(1).strip()
        
        return None

    def _get_latest_version(self, source_url: str, pattern: Optional[str] = None) -> Optional[str]:
        """Fetch latest version from source URL"""
        try:
            if 'github.com' in source_url:
                return self._get_github_latest_version(source_url)
            elif 'gitlab.com' in source_url:
                return self._get_gitlab_latest_version(source_url)
            elif 'dl.pstmn.io' in source_url:
                return self._get_postman_latest_version(source_url)
            else:
                # Try generic HTML parsing
                return self._parse_version_from_url(source_url, pattern)
        except Exception as e:
            print(f"  ⚠️  Error fetching version: {e}")
            return None

    def _get_github_latest_version(self, url: str) -> Optional[str]:
        """Get latest version from GitHub API"""
        # Extract owner/repo from various GitHub URL formats
        match = re.search(r'github\.com/([^/]+)/([^/]+)', url)
        if not match:
            return None
        
        owner, repo = match.groups()
        repo = repo.rstrip('/')
        
        api_url = f"https://api.github.com/repos/{owner}/{repo}/releases/latest"
        response = requests.get(api_url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            if 'tag_name' in data:
                version = data['tag_name'].lstrip('v')
                return version
        
        return None

    def _get_gitlab_latest_version(self, url: str) -> Optional[str]:
        """Get latest version from GitLab API"""
        match = re.search(r'gitlab\.com/([^/]+)/([^/]+)', url)
        if not match:
            return None
        
        owner, repo = match.groups()
        repo = repo.rstrip('/')
        
        # GitLab API requires URL encoding
        project_id = f"{owner}%2F{repo}"
        api_url = f"https://gitlab.com/api/v4/projects/{project_id}/releases/latest"
        response = requests.get(api_url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            if 'tag_name' in data:
                version = data['tag_name'].lstrip('v')
                return version
        
        return None

    def _get_postman_latest_version(self, url: str) -> Optional[str]:
        """Get latest Postman version"""
        # Postman versions can be fetched from their release page
        api_url = "https://www.postman.com/_api/core/versions"
        try:
            response = requests.get(api_url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                if isinstance(data, list) and len(data) > 0:
                    return data[0].get('version')
        except:
            pass
        
        return None

    def _parse_version_from_url(self, url: str, pattern: Optional[str] = None) -> Optional[str]:
        """Generic version parsing from HTML"""
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                if pattern:
                    match = re.search(pattern, response.text)
                    if match:
                        return match.group(1)
                # Try common version patterns
                match = re.search(r'(\d+\.\d+\.\d+)', response.text)
                if match:
                    return match.group(1)
        except:
            pass
        
        return None

    def _update_spec(self, package_name: str, new_version: str, config: Dict) -> bool:
        """Update .spec file with new version"""
        spec_file = REPO_ROOT / package_name / f"{package_name}.spec"
        
        if not spec_file.exists():
            return False
        
        try:
            with open(spec_file, 'r') as f:
                content = f.read()
            
            # Update Version field
            updated_content = re.sub(
                r'^Version:\s+.+$',
                f'Version:        {new_version}',
                content,
                count=1,
                flags=re.MULTILINE
            )
            
            # Reset Release to 1 when version changes
            updated_content = re.sub(
                r'^Release:\s+.+$',
                'Release:        %autorelease',
                updated_content,
                count=1,
                flags=re.MULTILINE
            )
            
            with open(spec_file, 'w') as f:
                f.write(updated_content)
            
            return True
        except Exception as e:
            print(f"  ⚠️  Error updating spec: {e}")
            return False

    def commit_changes(self):
        """Commit changes if any packages were updated"""
        if not self.updated_packages:
            print("\n✅ No updates needed")
            return
        
        try:
            # Stage all updated .spec files
            for package in self.updated_packages:
                spec_file = REPO_ROOT / package / f"{package}.spec"
                subprocess.run(['git', 'add', str(spec_file)], cwd=REPO_ROOT, check=True)
            
            # Create commit
            message = f"chore: update versions for {', '.join(self.updated_packages)}"
            subprocess.run(
                ['git', 'commit', '-m', message],
                cwd=REPO_ROOT,
                check=True
            )
            
            print(f"\n✅ Committed {len(self.updated_packages)} updated package(s)")
        except subprocess.CalledProcessError as e:
            print(f"\n⚠️  Error committing changes: {e}")


def main():
    checker = PackageChecker()
    checker.check_all_packages()
    checker.commit_changes()


if __name__ == '__main__':
    main()
