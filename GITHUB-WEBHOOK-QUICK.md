# GitHub Webhook Quick Reference

## Getting Started in 5 Minutes

### Step 1: Get COPR Webhook Info
```
1. Go to: https://copr.fedorainfracloud.org/coprs/[your-username]/
2. Click: Settings → Integrations (or scroll to Webhooks)
3. Find GitHub webhook section
4. Copy: <PROJECT_ID> and <WEBHOOK_TOKEN>
```

### Step 2: Add Webhook to GitHub
```
1. Go to: Your repository on GitHub
2. Click: Settings (top of repo)
3. Click: Webhooks (left sidebar, under "Code and automation")
4. Click: Add webhook (green button)
```

### Step 3: Fill Webhook Form

| Field | Value |
|-------|-------|
| **Payload URL** | `https://copr.fedorainfracloud.org/webhooks/github/<PROJECT_ID>/<WEBHOOK_TOKEN>/` |
| **Content type** | `application/json` |
| **Events** | ✅ Push events, ✅ Pull requests |
| **Active** | ✅ Checked |

### Step 4: Save & Verify
```
1. Click: Add webhook
2. Look for: Green ✓ checkmark in Recent Deliveries
3. If red X: Check URL for typos
```

### Step 5: Test It
```bash
git commit --allow-empty -m "test: trigger webhook"
git push origin main
# Wait 2-3 minutes, then check COPR builds
```

## Troubleshooting Checklist

- [ ] **URL correct?** No typos in PROJECT_ID or TOKEN
- [ ] **Active?** Checkmark next to "Active" is enabled
- [ ] **Events selected?** "Push events" is checked
- [ ] **Recent Deliveries?** Shows 200 OK responses
- [ ] **.spec file exists?** `package-name/package-name.spec` structure
- [ ] **COPR packages registered?** Check COPR project package list
- [ ] **Pushed to correct branch?** Usually `main` or `master`

## Common Errors

| Error | Fix |
|-------|-----|
| **404 Not Found** | Check PROJECT_ID and TOKEN from COPR |
| **Connection refused** | COPR servers may be down, try again later |
| **Webhook added but not firing** | Make sure "Active" checkbox is enabled |
| **Build not appearing** | Check COPR project has packages registered |

## View Recent Deliveries

```
GitHub repo → Settings → Webhooks → [Your webhook] → Recent Deliveries

Each delivery shows:
- Timestamp
- Status (200 = success, others = error)
- Response body (error details if failed)
```

## More Help

- Full guide: [WEBHOOK-SETUP.md](./WEBHOOK-SETUP.md)
- COPR docs: https://docs.copr.fedorainfracloud.org/user_documentation.html#webhooks
- GitHub webhook docs: https://docs.github.com/en/developers/webhooks-and-events/webhooks
