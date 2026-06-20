# COPR Webhook Integration Guide

## Overview

COPR webhooks provide a direct way to trigger builds when you push changes to GitHub or GitLab, bypassing the need for GitHub Actions intermediary.

**Advantages of webhooks:**
- Simpler setup (fewer secrets to manage)
- Faster build triggers (no GitHub Actions overhead)
- Direct source-to-COPR integration
- Lower cost (no CI/CD minutes used)

**Best for:** Projects where you want automatic builds on every push to main branch

## Setup Instructions

### 1. Get Your COPR Webhook URLs

From your COPR project page (https://copr.fedorainfracloud.org):

1. Go to **Settings** → **Integrations** (or scroll to "Webhooks" section)
2. You'll see webhook URLs for different platforms

Example format:
```
GitHub:  https://copr.fedorainfracloud.org/webhooks/github/<PROJECT_ID>/<WEBHOOK_TOKEN>/
GitLab:  https://copr.fedorainfracloud.org/webhooks/gitlab/<PROJECT_ID>/<WEBHOOK_TOKEN>/
Custom:  https://copr.fedorainfracloud.org/webhooks/custom/<PROJECT_ID>/<WEBHOOK_TOKEN>/<PACKAGE_NAME>/
```

**Note:** If you don't see webhook URLs, you may need to enable them in COPR project settings.

### 2. GitHub Webhook Setup (Step-by-Step)

> **⚡ Quick version?** See [GITHUB-WEBHOOK-QUICK.md](./GITHUB-WEBHOOK-QUICK.md) for 5-minute setup
> 
> **👁️ Visual guide?** See [GITHUB-WEBHOOK-SETUP-VISUAL.md](./GITHUB-WEBHOOK-SETUP-VISUAL.md) with diagrams and screenshots

#### Step 1: Navigate to Webhook Settings

1. Open your repository on GitHub
2. Click **Settings** (tab at the top of the repository)
3. On the left sidebar, click **Webhooks** (under "Code and automation" section)

#### Step 2: Add New Webhook

1. Click the green **Add webhook** button
2. You'll see a form to configure the webhook

#### Step 3: Configure Webhook Settings

Fill in the following fields:

**Payload URL** (most important):
```
https://copr.fedorainfracloud.org/webhooks/github/<PROJECT_ID>/<WEBHOOK_TOKEN>/
```
- Replace `<PROJECT_ID>` with your COPR project ID
- Replace `<WEBHOOK_TOKEN>` with your COPR webhook token
- Do NOT include a trailing comment or extra parameters

**Content type:**
- Select: **application/json** (from dropdown)

**Which events would you like to trigger this webhook?**
- Select: **Let me select individual events.** (radio button)

**Events to enable:**
- ✅ **Push events** (essential - triggers build on every push)
- ✅ **Pull requests** (optional - flags PR builds)
- ❌ Uncheck others (not needed for COPR builds)

**Active:**
- ✅ **Checked** (ensure this is enabled)

#### Step 4: Save Webhook

1. Click the green **Add webhook** button at the bottom
2. GitHub will send a test payload to COPR
3. You should see a green checkmark ✓ if successful

#### Verification

After adding the webhook, you'll see:
- Recent Deliveries section showing test delivery
- If green checkmark appears, the webhook is properly configured
- If red X appears, check:
  - Payload URL is correct (no typos)
  - URL is accessible from internet
  - COPR project is still active

#### Testing the Webhook

To verify the webhook works:

```bash
# Make a test commit and push
git commit --allow-empty -m "test: trigger webhook"
git push origin main
```

Then check:
1. **GitHub:** Settings → Webhooks → Recent Deliveries (should show success)
2. **COPR:** Project → Builds (new build should appear within 1-2 minutes)

#### GitHub Setup Example

Your webhook URL format will be:
```
https://copr.fedorainfracloud.org/webhooks/github/<PROJECT_ID>/<WEBHOOK_TOKEN>/
```

Replace the placeholders with your actual values from COPR settings.

### 3. GitLab Webhook Setup

1. Go to your repository on GitLab
2. Navigate to **Settings** → **Integrations** → **Webhooks**
3. Fill in:
   - **URL:** `https://copr.fedorainfracloud.org/webhooks/gitlab/<PROJECT_ID>/<WEBHOOK_TOKEN>/`
   - **Trigger:**
     - ✅ **Push events**
     - ✅ **Merge requests** (optional)
   - **SSL verification:** ✅ Enabled

4. Click **Add webhook**

### 4. Per-Package Webhooks (Optional)

If you want to trigger specific packages only:

```
GitHub:  https://copr.fedorainfracloud.org/webhooks/github/<PROJECT_ID>/<WEBHOOK_TOKEN>/<PKG_NAME>/
GitLab:  https://copr.fedorainfracloud.org/webhooks/gitlab/<PROJECT_ID>/<WEBHOOK_TOKEN>/<PKG_NAME>/
Custom:  https://copr.fedorainfracloud.org/webhooks/custom/<PROJECT_ID>/<WEBHOOK_TOKEN>/<PKG_NAME>/
```

Example for `postman` package:
```
https://copr.fedorainfracloud.org/webhooks/github/<PROJECT_ID>/<WEBHOOK_TOKEN>/postman/
```

## Configuration in Repository

Once webhooks are set up in COPR, no additional configuration is needed in your repository. However, to stay organized:

### 1. Document Your Webhook Setup

Create `.github/webhooks.md`:

```markdown
# COPR Webhook Configuration

## Registered Webhooks

| Platform | Type | Status | Last Updated |
|----------|------|--------|---------------|
| GitHub   | Push + PR | Active | YYYY-MM-DD |
| GitLab   | Push + MR | Active | YYYY-MM-DD |

## Webhook URLs

- **GitHub General:** `https://copr.fedorainfracloud.org/webhooks/github/<PROJECT_ID>/<WEBHOOK_TOKEN>/`
- **COPR Project:** `https://copr.fedorainfracloud.org/coprs/username/repo-name/`

(Replace `<PROJECT_ID>` and `<WEBHOOK_TOKEN>` with values from your COPR project settings)

## Testing Webhooks

After setup, test by making a commit:
```bash
git commit --allow-empty -m "test: trigger webhook"
git push origin main
```

Check COPR project for new build.
```

### 2. Monitor Webhook Delivery

On COPR, you'll see webhook history:
- Check if webhooks are received
- View delivery logs
- See which commits triggered builds

## Comparison: Webhooks vs GitHub Actions

| Feature | Webhooks | GitHub Actions |
|---------|----------|-----------------|
| Version Check | ❌ Manual | ✅ Automatic |
| Push to Build | ✅ Direct | ⚠️ Delayed |
| PR Flagging | ✅ Direct | ✅ Yes |
| Complexity | ⏹️ Simple | ⏹️ Complex |
| Cost | Free | Free (with limits) |
| Dependencies | COPR + GitHub | GitHub Actions runner |

**Recommendation:** 
- Use **webhooks** for simple automatic builds on push
- Use **GitHub Actions** if you need automatic version detection and updating

## Advanced: Combined Workflow

Use both for maximum automation:

1. **GitHub Actions** runs daily to check upstream versions
2. **Creates PR** with version updates
3. **Webhook** triggers builds automatically when PR is merged to main

This gives you:
- ✅ Automatic version detection
- ✅ Quick builds on merge
- ✅ Manual review of changes

## Troubleshooting

### GitHub Webhook Issues

**Problem: Webhook shows red X (failed delivery)**

1. Check URL is correct:
   ```
   https://copr.fedorainfracloud.org/webhooks/github/<PROJECT_ID>/<WEBHOOK_TOKEN>/
   ```
   - No trailing slashes except the last one
   - No extra parameters or comments
   - Check for typos in PROJECT_ID and TOKEN

2. Test the connection:
   - In GitHub: Settings → Webhooks → click on webhook → scroll to "Recent Deliveries"
   - Click on the failed delivery to see the error response
   - If it says "Connection refused" → COPR webhook server may be down
   - If it says "Not Found" (404) → URL is incorrect

3. Verify the webhook token:
   - Go back to COPR: Settings → Integrations → Webhooks
   - Copy the exact token (don't miss any characters)
   - Update GitHub webhook with the correct token

**Problem: Webhook shows green checkmark but no builds in COPR**

1. Check GitHub webhook delivery history:
   - Settings → Webhooks → Recent Deliveries
   - Should show successful POST requests (200 status code)

2. Check if the push actually triggered the webhook:
   - Make sure you pushed to a branch that COPR is watching
   - By default, COPR watches all branches
   - Check COPR project settings if specific branches are configured

3. Verify .spec file exists in correct location:
   ```
   /package-name/package-name.spec
   ```
   - COPR looks for spec file in package directory
   - If .spec file structure is wrong, webhook succeeds but build fails

4. Check COPR project settings:
   - COPR Project page → Package list
   - Verify at least one package is registered
   - If no packages, webhook won't trigger builds

**Problem: Only some packages build, not all**

- COPR webhook builds the package whose directory contains the modified .spec file
- If you modify multiple .spec files in one push, all should build
- If only one builds, check that other .spec files are in the correct directory structure

**How to Debug**

1. **Check GitHub webhook delivery:**
   ```
   GitHub repo → Settings → Webhooks → [Your Webhook]
       ↓ Recent Deliveries
       ↓ Click delivery to see request/response
   ```

2. **Check COPR webhook history:**
   ```
   COPR → Project Settings → Integrations → Webhooks
       ↓ Webhook History section
       ↓ Green ✓ = Received | Red X = Failed
   ```

3. **Check COPR builds:**
   ```
   COPR → Project page → Builds tab
       ↓ Look for recent builds
       ↓ Should show "Triggered by webhook" in build info
   ```

4. **Re-test webhook:**
   ```bash
   git commit --allow-empty -m "test: webhook"
   git push origin main
   # Wait 2-3 minutes, then check GitHub deliveries and COPR builds
   ```

### Common Webhook Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| Red X in Recent Deliveries | Wrong URL/token | Verify exact URL from COPR settings |
| 404 Not Found error | Incorrect PROJECT_ID or TOKEN | Copy fresh from COPR: Settings → Integrations |
| Connection timeout | Network/firewall issue | Check COPR status page or retry later |
| Green ✓ but no COPR build | .spec file not found | Ensure: `package-name/package-name.spec` structure |
| Only some packages build | Wrong directory structure | Check all modified .spec files are in their package directories |
| Webhook not firing at all | Webhook disabled/not active | GitHub: Settings → Webhooks → check "Active" box |

### General Troubleshooting Steps

1. **Verify .spec file syntax locally:**
   ```bash
   rpmlint package-name/package-name.spec
   ```

2. **Check directory structure is correct:**
   ```bash
   # Expected structure:
   postman/
   ├── postman.spec
   catppuccin-cursors/
   ├── catppuccin-cursors.spec
   ```

3. **Test webhook manually from GitHub:**
   - Settings → Webhooks → [Your webhook]
   - Scroll to Recent Deliveries
   - Click green dropdown → Redeliver
   - Watch for immediate 200 OK response

4. **Check COPR build logs:**
   - COPR → Builds → [failed build]
   - View build logs to see spec file parsing errors

## Security Considerations

- ✅ Webhook tokens are unique and revocable
- ✅ COPR validates source (GitHub/GitLab) 
- ⚠️ Anyone with repository push access can trigger builds
- 💡 Keep tokens in COPR (not in repo)

## See Also

- [COPR Webhook Documentation](https://docs.copr.fedorainfracloud.org/user_documentation.html#webhooks)
- [GitHub Webhooks Guide](https://docs.github.com/en/developers/webhooks-and-events/webhooks)
- [GitLab Webhooks Guide](https://docs.gitlab.com/ee/user/project/integrations/webhooks.html)
