# GitHub Webhook Documentation - Complete Index

Comprehensive guides for setting up COPR webhooks with GitHub.

## 📚 Documentation Files

### Quick Reference (Start Here!)
- **[GITHUB-WEBHOOK-QUICK.md](./GITHUB-WEBHOOK-QUICK.md)** ⚡
  - 5-minute setup guide
  - Simple checklist
  - Common errors table
  - Best for: First-time users in a hurry

### Visual Guide with Diagrams
- **[GITHUB-WEBHOOK-SETUP-VISUAL.md](./GITHUB-WEBHOOK-SETUP-VISUAL.md)** 👁️
  - Complete flow diagrams
  - Screenshot-style form layouts
  - Troubleshooting decision tree
  - Testing steps
  - Common mistakes table
  - Best for: Visual learners, detailed setup

### Full Detailed Documentation
- **[WEBHOOK-SETUP.md](./WEBHOOK-SETUP.md)** 📖
  - Complete step-by-step instructions
  - Detailed troubleshooting section
  - Webhook configuration options
  - Security considerations
  - Comparison with GitHub Actions
  - Best for: Comprehensive reference, advanced setup

### Related Guides
- **[CI-CD-SETUP.md](../CI-CD-SETUP.md)** - GitHub Actions alternative
- **[README.md](../README.md)** - Project overview and choosing between approaches

---

## 🎯 Which Guide Should I Use?

```
┌─────────────────────────────────────────┐
│ Are you new to webhooks?                │
└────────────┬──────────────────────────┬─┘
             │ YES                       │ NO
             ↓                           ↓
      Start with           Read full docs:
      QUICK.md            WEBHOOK-SETUP.md
             ↓
      Still confused?
             ↓
      View VISUAL.md
             ↓
      Can't find answer?
             ↓
      Check troubleshooting
      in WEBHOOK-SETUP.md
```

## ⏱️ Time Estimate

| Guide | Time | Best For |
|-------|------|----------|
| QUICK.md | 5 min | Quick setup |
| VISUAL.md | 15 min | Understanding the flow |
| WEBHOOK-SETUP.md | 30 min | Complete reference |
| All three | 45 min | Complete mastery |

## 🚀 30-Second Summary

1. **Get COPR webhook URL:** COPR → Settings → Integrations → Copy GitHub webhook URL
2. **Add to GitHub:** Repo → Settings → Webhooks → Add webhook → Paste URL
3. **Configure:** Content type = JSON, Events = Push + PR, Active = Checked
4. **Save and test:** Click Add → Check Recent Deliveries for ✓ status
5. **Verify:** Push code → Wait 2-3 min → Check COPR builds

Done! ✅

## 📋 Setup Checklist

- [ ] Got COPR webhook URL (PROJECT_ID and TOKEN)
- [ ] Found GitHub webhooks section (Settings → Webhooks)
- [ ] Filled in Payload URL without typos
- [ ] Set Content type to application/json
- [ ] Checked "Push events" and "Pull requests"
- [ ] Ensured "Active" checkbox is checked
- [ ] Saved webhook (Add webhook button)
- [ ] Saw green ✓ status in Recent Deliveries
- [ ] Tested with git push
- [ ] Verified build appeared in COPR

## 🆘 Troubleshooting Quick Reference

**Red X in Recent Deliveries?**
→ Check URL and TOKEN for typos in WEBHOOK-SETUP.md → Troubleshooting

**Webhook fires but no COPR build?**
→ Check .spec file structure: `package-name/package-name.spec`

**Build doesn't appear after 3+ minutes?**
→ Check COPR project has packages registered

**Still stuck?**
→ See Detailed troubleshooting in WEBHOOK-SETUP.md

## 📞 Need Help?

1. Check the appropriate guide above
2. Look for your issue in the guide's troubleshooting section
3. Verify URL, TOKEN, and .spec file structure
4. Try redeliver in GitHub webhook settings
5. Check COPR status: https://status.fedorainfracloud.org/

## 🔗 External Resources

- [COPR Webhooks Docs](https://docs.copr.fedorainfracloud.org/user_documentation.html#webhooks)
- [GitHub Webhooks Docs](https://docs.github.com/en/developers/webhooks-and-events/webhooks)
- [GitHub Webhook API](https://docs.github.com/en/developers/webhooks-and-events/webhooks/webhook-events-and-payloads)

---

**Choose your guide above and start with either QUICK.md or VISUAL.md!**
