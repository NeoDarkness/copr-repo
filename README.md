# COPR Repository CI/CD Pipeline

Automated build system for COPR packages with multiple CI/CD options.

## 🚀 Quick Start

Choose your CI/CD approach:

### 1. **Webhooks** (Fast & Simple) ⚡
Direct GitHub/GitLab → COPR builds with no intermediary.
```bash
cat WEBHOOK-SETUP.md
```
- **Pros:** Simple, fast, free, fewer secrets
- **Cons:** Manual version updates
- **Best for:** Rapid iteration on package specs

### 2. **GitHub Actions** (Full Automation) 🤖
Automatic version detection + builds + PRs for review.
```bash
bash scripts/setup.sh
```
- **Pros:** Fully automated, manual review gates
- **Cons:** More complex, more secrets needed
- **Best for:** Hands-off continuous updates

### 3. **Combined** (Recommended) 🔄
Use both: GitHub Actions for version checks → Webhooks for builds
- **Best of both worlds:** Automation + simplicity

## 📁 Project Structure

```
.github/
  workflows/
    check-updates.yml      # Daily version checks
    build-on-merge.yml     # Build on spec changes
packages.yml               # Package source config
scripts/
  check_updates.py         # Version detection
  setup.sh                 # GitHub Actions setup
  update-now.sh            # Manual update trigger
  webhook-urls.sh          # Webhook reference
CI-CD-SETUP.md            # GitHub Actions guide
WEBHOOK-SETUP.md          # Webhook integration guide
```

## 📖 Documentation

- **[CI-CD-SETUP.md](CI-CD-SETUP.md)** - GitHub Actions configuration
- **[WEBHOOK-SETUP.md](WEBHOOK-SETUP.md)** - Webhook integration
- **[packages.yml](packages.yml)** - Package sources

## 🔧 Setup Commands

```bash
# Setup GitHub Actions
bash scripts/setup.sh

# View webhook URLs
bash scripts/webhook-urls.sh

# Manually check for updates
bash scripts/update-now.sh

# View package configuration
cat packages.yml
```

## 🏗️ Architecture

### GitHub Actions Approach
```
Scheduled Check (2 AM UTC)
    ↓
check_updates.py (Python)
    ↓
Detect Upstream Updates
    ↓
Update .spec files
    ↓
Create Pull Request
    ↓
(Manual Review)
    ↓
Merge to main
    ↓
build-on-merge.yml triggers
    ↓
COPR Build
```

### Webhook Approach
```
Push to GitHub/GitLab
    ↓
Webhook triggers COPR
    ↓
COPR Build (immediate)
```

### Combined Approach
```
Scheduled Check + Webhook Build
    ↓
Daily version updates via GitHub Actions
    ↓
Manual review of changes
    ↓
Merge activates webhook
    ↓
Instant COPR build
```

## 🔐 Security

### GitHub Actions Requires
- `COPR_USERNAME`
- `COPR_LOGIN`
- `COPR_TOKEN`
- `COPR_REPO`

[See CI-CD-SETUP.md for secure configuration]

### Webhooks Require
- COPR Project ID
- Webhook Token (from COPR)

[See WEBHOOK-SETUP.md for security notes]

## 🧪 Testing Locally

```bash
# Test version checking (GitHub Actions approach)
source .venv/bin/activate
python3 scripts/check_updates.py

# Test webhooks
bash scripts/webhook-urls.sh
```

## 📊 Comparison

| Feature | Webhooks | GitHub Actions |
|---------|----------|---|
| Automatic version detection | ❌ | ✅ |
| Automatic builds on push | ✅ | ✅ |
| PR creation/review | ❌ | ✅ |
| Requires CI secrets | ❌ | ✅ |
| Build speed | ⚡ Fast | ⏱️ Slower |
| Configuration complexity | Simple | Complex |
| Best for | Simple builds | Complex workflows |

## 🆘 Troubleshooting

### GitHub Actions
See [CI-CD-SETUP.md - Troubleshooting](CI-CD-SETUP.md#troubleshooting)

### Webhooks
See [WEBHOOK-SETUP.md - Troubleshooting](WEBHOOK-SETUP.md#troubleshooting)

## 📚 Resources

- [COPR Webhooks Docs](https://docs.copr.fedorainfracloud.org/user_documentation.html#webhooks)
- [GitHub Actions Docs](https://docs.github.com/actions)
- [GitLab Webhooks Docs](https://docs.gitlab.com/ee/user/project/integrations/webhooks.html)
- [RPM Spec Guide](https://rpm-packaging-guide.github.io/)

---

**Choose your approach above and follow the corresponding documentation!**
