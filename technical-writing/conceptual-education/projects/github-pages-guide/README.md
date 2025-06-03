# 🧭 GitHub Pages User Guide: From Confusion to Clarity

> *"Built from real 404s, broken links, and documentation despair."*  
> A beginner-friendly guide to setting up and publishing GitHub Pages—step-by-step, mistake-by-mistake.

---

## 📘 Table of Contents

- [What Is GitHub Pages?](#what-is-github-pages)  
- [How GitHub Pages Actually Works](#how-github-pages-actually-works)  
- [Step-by-Step: Creating Your First GitHub Pages Site](#step-by-step-creating-your-first-github-pages-site)  
- [Choosing Between README.md and index.md](#choosing-between-readmemd-and-indexmd)  
- [Where to Put Your Files (And What Breaks Things)](#where-to-put-your-files-and-what-breaks-things)  
- [The .nojekyll File Mystery](#the-nojekyll-file-mystery)  
- [Why You Got a 404 (And What to Do About It)](#why-you-got-a-404-and-what-to-do-about-it)  
- [Permalinks: Your Invisible Gatekeepers](#permalinks-your-invisible-gatekeepers)  
- [Relative Links: ./, ../, and the Blob Confusion](#relative-links---and-the-blob-confusion)  
- [Live Site Preview vs GitHub Repo Preview](#live-site-preview-vs-github-repo-preview)  
- [Advanced: Using Custom Workflows and gh-pages Branch](#advanced-using-custom-workflows-and-gh-pages-branch)  
- [Troubleshooting Cheatsheet](#troubleshooting-cheatsheet)  
- [Real-World Mistakes We Made (So You Don’t)](#real-world-mistakes-we-made-so-you-dont)

---

## What Is GitHub Pages?

GitHub Pages is a free service by GitHub that lets you turn a GitHub repository into a live, static website. It’s widely used for:

- Portfolios
- Project documentation
- Developer blogs
- Open-source project landing pages

You don't need to install anything or deploy manually. You simply write Markdown or HTML, push it to your repo, and GitHub Pages takes care of the rest.

---

## How GitHub Pages Actually Works

Behind the scenes:

- GitHub watches a specific **branch** and **folder** in your repo.
- It passes your Markdown files (`.md`) through **Jekyll**, a static site generator.
- Jekyll converts them to `.html` and serves them as a website.
- If you're using `/docs/index.md`, it becomes your live homepage (`index.html`).

---

## Step-by-Step: Creating Your First GitHub Pages Site

1. Go to your GitHub repo → **Settings → Pages**
2. Set your Source:
   - **Branch**: `main`
   - **Folder**: `/docs` or `/` (root)
3. Click **Save**
4. Create a file called `docs/index.md` and add:

   ```markdown
   # Welcome
   This is my GitHub Pages site.
   ```

5. Commit the file and wait ~30 seconds
6. GitHub will show a link to your live website under "GitHub Pages → Your site is published at..."

✅ That’s it! Your site is live.

---

## Choosing Between README.md and index.md

| File        | Purpose                  | Rendered Where                    |
|-------------|--------------------------|-----------------------------------|
| `README.md` | GitHub repo homepage     | Shown when you visit the repo     |
| `index.md`  | GitHub Pages homepage    | Served on the actual website URL  |

If you create only `README.md`, it looks great in the GitHub repo—but your live site may 404.  
If you want to serve a homepage via GitHub Pages, use `index.md` inside your `/docs/` folder.

---

## Where to Put Your Files (And What Breaks Things)

Your content must live inside the folder specified in GitHub Pages settings.

Most commonly:
- Set source as `/docs` on the `main` branch
- All `.md` files (e.g., `index.md`, `STYLE-GUIDE/index.md`) must live inside `docs/`

**Example Mistake:**  
You link to `../STYLE-GUIDE/index.md` from `docs/index.md`  
❌ This fails because `../STYLE-GUIDE/` is outside the published folder.

✅ Correct:  
Put `STYLE-GUIDE/` inside `docs/`, and link as `STYLE-GUIDE/index.html`.

---

## The .nojekyll File Mystery

`.nojekyll` is a special file you place at the root of your site to disable Jekyll.

- ✅ Use it if you want to serve raw HTML, or folders that begin with `_`
- ❌ Don’t use it if you're relying on Jekyll features (like Markdown rendering)

Most users using `index.md` and other Markdown don’t need `.nojekyll`.

---

## Why You Got a 404 (And What to Do About It)

404s are common during setup. Here’s how to troubleshoot:

### Homepage 404  
You may not have a valid `index.md` in your `/docs` folder. GitHub looks for this file and converts it into `index.html`.

### Page-level 404  
You may be linking to `.md` files instead of `.html`. GitHub Pages renders `.md` → `.html`, and visitors can’t load the Markdown file directly.

---

## Permalinks: Your Invisible Gatekeepers

To serve `docs/STYLE-GUIDE/index.md` at `/STYLE-GUIDE/`, add this to the top of the file:

```yaml
---
permalink: /STYLE-GUIDE/
---
```

This tells Jekyll to generate your page as `/STYLE-GUIDE/index.html`.  
Without this, clean folder links won’t work.

---

## Relative Links: `./`, `../`, and the Blob Confusion

✅ Use relative links inside your Pages site:

```markdown
[Style Guide](./STYLE-GUIDE/index.html)
```

- `./` = current folder
- `../` = one level up

❌ Never link to GitHub’s `blob/main` URLs.  
They only work on GitHub.com and break on the live site.

---

## Live Site Preview vs GitHub Repo Preview

| Preview Context | What You See               |
|-----------------|----------------------------|
| GitHub Repo     | Renders `.md` in browser   |
| GitHub Pages    | Converts `.md` to `.html`  |

That’s why a link like `docs/STYLE-GUIDE/index.md` works inside the GitHub repo, but fails on the live site.  
You must link to `index.html` or use permalinks.

---

## Advanced: Using Custom Workflows and gh-pages Branch

For more control, you can deploy using GitHub Actions and a `gh-pages` branch.

```yaml
name: Deploy GitHub Pages
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./docs
```

Use this if you want to separate your site files from your source.

---

## Troubleshooting Cheatsheet

| Problem                            | Likely Cause                        | Fix                                           |
|------------------------------------|--------------------------------------|-----------------------------------------------|
| 404 on homepage                    | Missing `index.md` in `/docs/`      | Create `docs/index.md`                        |
| Internal links work in repo only   | Linking to `.md` not `.html`        | Use `.html` paths or add permalinks           |
| Clean URLs not working             | Missing front-matter in index file  | Add `--- permalink: /path/ ---`               |
| Pages not updating after commit    | GitHub Actions misfire or delay     | Wait 1–2 mins or check Actions tab            |

---

## Real-World Mistakes We Made (So You Don’t)

### Mistake 1: Linked to `README.md` instead of `index.md`  
**Result**: Repo preview worked. Live site 404’d.  
**Fix**: Created `docs/index.md`

---

### Mistake 2: Linked to `./STYLE-GUIDE/` instead of `index.html`  
**Result**: Repo link worked, live site failed.  
**Fix**: Changed links to `STYLE-GUIDE/index.html`

---

### Mistake 3: Missing front-matter  
**Result**: Clean URLs didn’t resolve properly.  
**Fix**: Added this to top of the file:

```yaml
---
permalink: /STYLE-GUIDE/
---
```

---

### Mistake 4: Folder outside `docs/`  
**Result**: File wasn’t published at all.  
**Fix**: Moved everything into `docs/`

---

## Final Note

GitHub Pages is powerful once you understand how it works. But it can be frustrating when links break without explanation.

This guide exists because we broke things first—so you don’t have to.

> **Don't assume**:  
> Always test your links *on the live site*, not just inside the repo.

---

**Author:** Shailesh Rawat  
**Repo:** [sans-serif-sentiments](https://github.com/ShaileshRawat1403/sans-serif-sentiments)
