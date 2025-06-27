# 🛠️ Troubleshooting Guide

*Run into issues while using GitBook? Start here to resolve the most common problems without delay.*

This guide helps you identify, diagnose, and resolve the most frequently reported challenges when using GitBook—across setup, writing, syncing, and publishing workflows.

---

## 🔄 GitHub/GitLab Sync Issues

**Problem:** Changes in GitHub don’t reflect in GitBook, or vice versa.

**What to Check:**
- Ensure your GitHub/GitLab integration is connected.  
- Confirm that you’ve **enabled syncing** in your space settings.  
- Check the repo permissions on your connected account.  
- Review for any recent GitHub API rate limits or permission errors.

📎 **Related:** [Setup Guide →](../gitbook-setup-guide/README.md#connect-github-or-gitlab)

🖼️ *[Insert screenshot showing sync settings toggle]*

---

## ✏️ Editor Not Saving Changes

**Problem:** Changes made in the editor appear to be lost or not saved.

**Try This:**
- Refresh the page. GitBook auto-saves, but you may have encountered a UI lag.
- Check your browser console for extension conflicts.
- Use the version history to restore the last good save.

📎 **Related:** [Editor Guide →](../gitbook-editor-guide/README.md#using-the-editor)

🖼️ *[Insert screenshot of version history drawer]*

---

## 📂 Sidebar or Page Navigation Missing

**Problem:** Sidebar doesn’t appear or pages seem to disappear.

**What Might Help:**
- Review your **navigation configuration** in space settings.
- Confirm that pages are not accidentally unpublished or nested.
- Switch to structure view to manually reorder and re-link pages.

📎 **Related:** [Setup Guide →](../gitbook-setup-guide/README.md#configure-sidebar)

🖼️ *[Insert screenshot of sidebar settings or structure view]*

---

## 📤 Publishing Issues (Page Not Visible)

**Problem:** You’ve published a space but the page isn't accessible via link.

**Steps to Check:**
- Confirm the **page is marked as “published.”**
- Check access permissions—ensure space visibility is set to **Public**.
- If using custom domains, verify DNS settings have propagated.

📎 **Related:** [Getting Started →](../gitbook-getting-started/README.md#publish-your-space)

🖼️ *[Insert screenshot of publish button and visibility dropdown]*

---

## 🧩 Embedded Content Not Displaying

**Problem:** You’ve added embeds (e.g., YouTube, Google Docs), but they don’t render.

**What To Do:**
- Ensure the embed URL is **publicly accessible**.
- Confirm you’re using a supported block type (e.g., iframe, embed).
- For Markdown mode, use proper embed syntax.

📎 **Related:** [Editor Guide →](../gitbook-editor-guide/README.md#embed-content)

🖼️ *[Insert screenshot showing embed block config]*

---

## 🧪 Still Stuck?

If these fixes don’t help:
- Visit [GitBook Help Center](https://support.gitbook.com/)
- Reach out via their [official contact page](https://www.gitbook.com/contact)

📎 **You may also want to consult:**  
- [Overview →](../gitbook-overview/README.md#product-limitations)  
- [Glossary →](../gitbook-glossary/README.md) for terms like “Publish,” “Space,” and “Embed.”

---

✅ *All screenshots mentioned above can be captured during actual usage or sourced from your own testing. Insert them inline in your GitBook export version.*

