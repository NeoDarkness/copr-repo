# GitHub Webhook Setup - Visual Guide

## Complete Flow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│ 1. Get Information from COPR                                 │
├─────────────────────────────────────────────────────────────┤
│ https://copr.fedorainfracloud.org/coprs/[username]/          │
│         ↓                                                      │
│ Settings → Integrations → Webhooks Section                   │
│         ↓                                                      │
│ Copy: PROJECT_ID and WEBHOOK_TOKEN                           │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ 2. Add Webhook to GitHub Repository                          │
├─────────────────────────────────────────────────────────────┤
│ Your Repository on GitHub                                    │
│         ↓                                                      │
│ Settings → Webhooks                                          │
│         ↓                                                      │
│ Add webhook                                                   │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ 3. Configure Webhook                                         │
├─────────────────────────────────────────────────────────────┤
│ Payload URL:                                                 │
│ https://copr.fedorainfracloud.org/webhooks/github/           │
│ <PROJECT_ID>/<WEBHOOK_TOKEN>/                                │
│                                                               │
│ Content type: application/json                               │
│ Events: ✅ Push, ✅ Pull requests                             │
│ Active: ✅ Checked                                            │
│         ↓                                                      │
│ Save webhook                                                  │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ 4. Verify Webhook                                            │
├─────────────────────────────────────────────────────────────┤
│ GitHub shows "Recent Deliveries"                             │
│         ↓                                                      │
│ Look for green ✓ status (200 OK)                             │
│ OR red ✗ if there's an error                                 │
│         ↓                                                      │
│ If error: Check URL and token for typos                      │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ 5. Test by Pushing Code                                      │
├─────────────────────────────────────────────────────────────┤
│ $ git push origin main                                       │
│         ↓                                                      │
│ GitHub sends webhook to COPR                                 │
│         ↓ (2-3 minutes)                                       │
│ COPR starts build automatically                              │
│         ↓                                                      │
│ Check: https://copr.fedorainfracloud.org/builds/            │
└─────────────────────────────────────────────────────────────┘
```

## Step-by-Step Screenshots Guide

### STEP 1: Get COPR Webhook URL

```
🔗 https://copr.fedorainfracloud.org/coprs/your-username/
        ↓ Look for "Settings" button
        ↓ Click on "Integrations" section
        ↓ Scroll to "Webhooks" section
        
You'll see:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
GitHub:
https://copr.fedorainfracloud.org/webhooks/github/[PROJECT_ID]/[TOKEN]/

GitLab:
https://copr.fedorainfracloud.org/webhooks/gitlab/[PROJECT_ID]/[TOKEN]/
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Copy the full GitHub webhook URL
```

### STEP 2: Go to GitHub Webhooks

```
🔧 https://github.com/your-username/copr-repo/settings/hooks
        ↓
You'll see: "Webhooks" in left sidebar
        ↓
        (If not visible, make sure you're in "Settings" tab)
        ↓
        Click "Settings" → Scroll left sidebar down
        ↓
        Look for "Code and automation" section
        ↓
        Under it: "Webhooks"
```

### STEP 3: Add New Webhook

```
🟢 Click "Add webhook" button

Then fill in the form:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Payload URL *
┌──────────────────────────────────────────────────┐
│ Paste the COPR webhook URL here:                 │
│                                                   │
│ https://copr.fedorainfracloud.org/webhooks/      │
│ github/[PROJECT_ID]/[TOKEN]/                     │
└──────────────────────────────────────────────────┘

Content type *
┌──────────────────────────────────────────────────┐
│ ⬇ dropdown → Select "application/json"           │
└──────────────────────────────────────────────────┘

Which events would you like to trigger this webhook?
┌──────────────────────────────────────────────────┐
│ ◉ Let me select individual events.                │
│ (select this option)                              │
└──────────────────────────────────────────────────┘

Individual events:
┌──────────────────────────────────────────────────┐
│ ✅ Push events                                    │
│ ✅ Pull requests                                  │
│ ☐ (uncheck others)                               │
└──────────────────────────────────────────────────┘

Active
┌──────────────────────────────────────────────────┐
│ ☑ Active                                          │
│ (make sure this is checked)                       │
└──────────────────────────────────────────────────┘

🟢 Click "Add webhook" button
```

### STEP 4: Verify Success

```
GitHub shows "Recent Deliveries" section

If you see:
  ✅ Green circle with status "200" → SUCCESS!
  ❌ Red X with status "404" → URL error (check PROJECT_ID/TOKEN)
  ❌ Red X with "Connection refused" → COPR server issue

If green ✓ but no COPR builds:
  → Check .spec file path: package-name/package-name.spec
  → Check COPR project has packages registered
```

## Testing the Webhook

### Make a Test Commit

```bash
# Go to repository
cd /home/aldi/Projects/Local/copr-repo

# Make empty test commit
git commit --allow-empty -m "test: trigger webhook"

# Push to main
git push origin main

# ⏱️ Wait 2-3 minutes
```

### Check GitHub Webhook Fired

```
GitHub Repo → Settings → Webhooks → [Your Webhook]
                ↓
            Look at "Recent Deliveries" section
                ↓
        Should show 1-2 recent POST requests
                ↓
            If status is 200 → webhook worked!
            If status is 404 → check URL
```

### Check COPR Build Started

```
COPR → https://copr.fedorainfracloud.org
        ↓
    Your Project → Builds tab
        ↓
    Should show new build from last 5 minutes
        ↓
    If build shows "postman" → it worked!
```

## Troubleshooting Decision Tree

```
        Does GitHub show red X in Recent Deliveries?
                    ↙                ↘
                YES                  NO
                 ↓                    ↓
            Check error message   Check COPR builds
                 ↓                    ↓
         "404 Not Found"?        Any new builds?
              ↙       ↘              ↙       ↘
            YES        NO          YES       NO
             ↓          ↓           ↓         ↓
          FIX:        FIX:         ✅      FIX:
          Check      Connection   OK!     Check
          URL        issue or              .spec
          typo       COPR down             file
```

## Common Setup Mistakes

| ❌ Wrong | ✅ Correct | Problem |
|---------|----------|---------|
| `https://copr.../webhooks/github/<ID>/<TOKEN>` (no /) | `https://copr.../webhooks/github/<ID>/<TOKEN>/` (with /) | Trailing slash missing |
| `https://copr.../webhooks/github/<ID>/<TOKEN>?test` | `https://copr.../webhooks/github/<ID>/<TOKEN>/` | Extra parameters |
| Copy-paste but skip one character | Double-check for typos | Token incomplete |
| content-type: "application/x-www-form-urlencoded" | content-type: "application/json" | Wrong content type |
| ☐ Active (unchecked) | ☑ Active (checked) | Webhook disabled |
| Select all events | Select only: Push, Pull requests | Too many events |

## Quick Status Check

```bash
# After adding webhook, test with:
git commit --allow-empty -m "test"
git push origin main

# Then immediately check:
# 1. GitHub: Settings → Webhooks → Recent Deliveries
# 2. COPR: Builds → Look for new build
# 3. If both show activity → ✅ Setup complete!
```

See [WEBHOOK-SETUP.md](./WEBHOOK-SETUP.md) for full documentation.
