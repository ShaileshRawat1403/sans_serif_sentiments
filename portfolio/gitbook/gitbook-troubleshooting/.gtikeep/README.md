# 🛠️ Troubleshooting Guide: Common GitBook Issues

Use this guide to identify and resolve common issues you may encounter while using GitBook.  
Each section includes a symptom, likely cause, and recommended actions.

---

## 🔒 Problem: I Can’t Access a Space

**Possible Causes:**
- You’re not logged in with the correct workspace account  
- The space is set to **Private**, and you haven’t been added as a member  
- Your role doesn’t include access to that space

**What to Do:**
- Confirm you’re signed in to the correct account  
- Ask the workspace admin to verify your access level  
- Check the visibility settings for the space under **Space Settings → Access**

> 🖼️  
> ![GitBook space access settings showing private/public toggles](images/gitbook-space-access-settings.png)

---

## 🌐 Problem: My Published Page Isn’t Visible

**Possible Causes:**
- The space hasn’t been published  
- The page is in **Draft** mode  
- You're viewing the wrong workspace URL

**What to Do:**
- Confirm that the space is published (look for the globe icon beside the space name)  
- Go to the page and click **Publish** if it's still a draft  
- Check that you're sharing the correct public URL from the top-right **Share** menu

> 📘 Tip: Every GitBook space has a unique URL, even if multiple spaces are in the same workspace.

---

## ⏳ Problem: My Changes Aren’t Saving

**Possible Causes:**
- You may have lost connection temporarily  
- A sync conflict occurred while multiple users edited the same content  
- You’re using an unsupported browser or an extension blocking GitBook

**What to Do:**
- Refresh the page and re-authenticate if prompted  
- Use **GitBook’s autosave** — edits are saved in real-time; no manual save needed  
- Try switching to another browser (Chrome or Firefox recommended)

> ⚠️ Note: GitBook does not support Internet Explorer or very old browser versions.

---

## 🔄 Problem: I Can’t Switch Between Markdown and Block Mode

**Possible Causes:**
- You’re working in a synced GitHub doc (external sources lock the editing mode)  
- Some formatting elements may not be convertible automatically  
- You’re viewing the page as a viewer or guest, not as an editor

**What to Do:**
- Confirm you have **Editor** or **Admin** role in the workspace  
- Check if the page is synced from GitHub — editing must be done externally  
- If mode switching is blocked, copy content and create a new page in the desired mode

> 🖼️  
> ![Editor settings showing mode toggle option](images/gitbook-editor-mode-toggle.png)

---

## 🚫 Problem: I Invited a Team Member, But They Can’t See Anything

**Possible Causes:**
- The invite hasn’t been accepted yet  
- They were added as a **Viewer** but the space is still **Private**  
- Their email was entered incorrectly

**What to Do:**
- Resend the invitation under **Workspace Settings → Members**  
- Verify their role and space-level access  
- Ask them to check spam or promotional folders for the invite email

---

## ✅ General Tips

- Always use the latest version of your browser  
- GitBook autosaves, but check for internet disconnects if edits seem lost  
- Recheck space and page visibility before assuming content was deleted  
- Use the **GitBook Docs** site for platform status or known issues

> 🔗 [Visit GitBook Status Page](https://status.gitbook.com/)  
> 🔗 [Official GitBook Support](https://docs.gitbook.com/help)

---

## ➕ Next Steps

- [Explore the Glossary →](./gitbook-glossary.md)  
- [Use the Editor →](./gitbook-editor-guide.md)
