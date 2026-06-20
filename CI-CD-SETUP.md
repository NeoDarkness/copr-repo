# CI/CD Setup Guide

## Overview

This repository provides multiple CI/CD approaches:

### Option 1: GitHub Actions (Recommended for version auto-updates)
- **Check for upstream updates** daily (configurable schedule)
- **Update .spec files** with new versions automatically
- **Build packages in COPR** when changes are merged
- **Create pull requests** for manual review
- Best for: Complete automation with manual review gates

### Option 2: COPR Webhooks (Simpler, faster builds)
- **Direct GitHub/GitLab → COPR integration**
- **Automatic builds on push** without CI runner overhead
- **Less configuration** needed
- Best for: Simple workflows focused on building

**See [WEBHOOK-SETUP.md](./WEBHOOK-SETUP.md) for webhook-based setup.**

Choose based on your needs:
- 🤖 **Full automation** (version checking + building) → Use GitHub Actions
- ⚡ **Fast builds on push** → Use Webhooks
- 🔄 **Both** → Use webhooks for builds + GitHub Actions for version checks

## Quick Start

### 1. Initial Setup

```bash
# Clone and enter the repository
cd /home/aldi/Projects/Local/copr-repo

# Run setup script
bash scripts/setup.sh
```

### 2. Configure GitHub Secrets

Add these secrets to your GitHub repository settings (Settings → Secrets and variables → Actions):

- **COPR_USERNAME**: Your COPR username
- **COPR_LOGIN**: Your COPR login token (from ~/.config/copr)
- **COPR_TOKEN**: Your COPR API token
- **COPR_REPO**: Your COPR repository (format: `username/repo-name`)

To get your COPR tokens:

1. **Via COPR Web UI** (Recommended):
   - Go to https://copr.fedorainfracloud.org
   - Click on your username (top right) → **API**
   - Copy your **login** and **token**
   - Your **username** is shown on the same page

2. **Via Config File** (if you have one):
   ```bash
   cat ~/.config/copr
   ```
   If the file doesn't exist, use method 1 above.

3. **Get Repository Name**:
   - Go to your COPR project settings
   - Format: `[your-username]/[your-repo-name]`

### 3. Configure Package Sources

Edit `packages.yml` to configure which packages to monitor:

```yaml
packages:
  package-name:
    source_url: https://github.com/owner/repo  # or other source
    version_pattern: null  # optional regex pattern
    enabled: true
```

## Workflows Explained

### check-updates.yml (Daily Scheduled)
- Runs every day at 2 AM UTC (configurable)
- Checks each package's upstream source for new versions
- Updates .spec files if newer versions found
- Creates a pull request for review

### build-on-merge.yml (On Push)
- Triggers when .spec files are changed and merged to main
- Detects which packages changed
- Builds them in your COPR repository
- Comments on PR with build status

## Local Testing

Test the update checker locally before relying on GitHub Actions:

```bash
# Activate virtual environment
source .venv/bin/activate

# Run update checker
python3 scripts/check_updates.py

# Or use the helper script
bash scripts/update-now.sh
```

## Manual Update Trigger

To manually check for updates outside the scheduled time:

```bash
# Method 1: Use the manual script
bash scripts/update-now.sh

# Method 2: Push to trigger GitHub Actions
# (automatic on push to main)

# Method 3: Manually trigger via GitHub UI
# Go to Actions → Check Upstream Updates → Run workflow
```

## Supported Version Sources

The `check_updates.py` script supports:
- **GitHub**: Automatic release detection
- **GitLab**: Automatic release detection
- **Postman**: Direct API
- **Generic HTTP**: Custom regex patterns

## Troubleshooting

### No updates detected
- Check if `packages.yml` has the correct source URLs
- Run locally: `python3 scripts/check_updates.py`
- Verify internet connectivity to source URLs

### COPR build fails
- Verify COPR secrets are set correctly
- Check if .spec file is valid: `rpmlint package/*.spec`
- View build logs in COPR web UI

### GitHub Actions not running
- Check if workflows are enabled: Settings → Actions → General
- Verify branch protection rules don't block automated PRs
- Check workflow logs: Actions tab → Check Upstream Updates

## Customization

### Change check schedule
Edit `.github/workflows/check-updates.yml`:
```yaml
schedule:
  - cron: '0 2 * * *'  # Change this line
```

Cron format: `minute hour day month day-of-week`
- `0 0 * * *` = Daily at midnight
- `0 */6 * * *` = Every 6 hours
- `0 12 * * 0` = Weekly on Sunday at noon

### Add custom version patterns
For sources that don't support GitHub/GitLab APIs:

```yaml
packages:
  mypackage:
    source_url: https://example.com/releases
    version_pattern: 'v(\d+\.\d+\.\d+)'  # Regex pattern
    enabled: true
```

### Auto-merge updates
Uncomment in `build-on-merge.yml` to enable auto-merge on successful builds.

## Security Notes

- Never commit COPR credentials to the repository
- Use GitHub Secrets for all sensitive data
- Review PRs before merging to ensure changes are correct
- Consider adding approval requirement for automated PRs

## File Structure

```
.github/
  workflows/
    check-updates.yml      # Scheduled version check
    build-on-merge.yml     # Build on version update
packages.yml               # Package configuration
scripts/
  check_updates.py         # Update checking script
  setup.sh                 # Setup script
  update-now.sh            # Manual trigger script
```

## Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/actions)
- [COPR Documentation](https://docs.pagure.org/copr.copr/)
- [RPM Spec File Guide](https://rpm-packaging-guide.github.io/)
