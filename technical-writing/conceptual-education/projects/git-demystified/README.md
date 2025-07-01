# git-demystified


_A calm, clear, human-first walk-through of the Git pull/push/rebase workflow, with analogies anyone can relate to._

##  Table of Contents


1. [Why Git?](./#why-git)
2. [Key Concepts](./#key-concepts)
3. [Basic Commands](./#basic-commands)
4. [Daily Workflow](./#daily-workflow)
5. [Rebase vs. Merge](./#rebase-vs-merge)
6. [Handling Conflicts](./#handling-conflicts)
7. [Best Practices](./#best-practices)
8. [Troubleshooting](./#troubleshooting)
9. [Glossary](./#glossary)

***

## Why Git?


Imagine you’re writing a long letter by hand. Every time you finish a paragraph, you make a photocopy—just in case you spill coffee or want to go back. Git does that automatically for your text files.

* **Version history** = your stack of photocopies
* **Rollback** = grabbing an older copy when something spills

> 💡 **Analogy:** Git is like a time-traveling camera that snaps a picture every time you hit _Save_.

***

## Key Concepts


| Term                  | What It Means                                                           |
| --------------------- | ----------------------------------------------------------------------- |
| **Repository (repo)** | A folder that holds your project’s files and history.                   |
| **Local repo**        | The copy of the repo on your computer.                                  |
| **Remote repo**       | The “official” copy on GitHub (or another server).                      |
| **origin**            | The nickname for your default remote repo on GitHub.                    |
| **Branch**            | A parallel version of your repo (e.g. `main`, `feature/button-fix`).    |
| **Commit**            | A snapshot of your changes with a message explaining _what_ you did.    |
| **Staging area**      | Where you “select” which changes to include in your next commit.        |
| **Pull**              | Fetch new commits from GitHub _and_ merge them into your local branch.  |
| **Push**              | Send your local commits up to GitHub so others can see them.            |
| **Fetch**             | Download new commits from GitHub _without_ merging them yet.            |
| **Merge**             | Combine two branches’ histories into one (can create a “merge commit”). |
| **Rebase**            | Replay your local commits on top of fetched commits—rewrites history.   |

### Some Analogies


| Term            | Real-world Analogy                                    |
| --------------- | ----------------------------------------------------- |
| **Local repo**  | Your home office (your computer folder)               |
| **Remote repo** | The post office (GitHub) where everyone’s copies live |
| **Branch**      | A side road off the main highway                      |
| **Commit**      | Sealing an envelope with today’s changes              |
| **Stage**       | Laying letters on your desk before sealing            |
| **Fetch**       | Checking the mailbox for new mail                     |
| **Pull**        | Checking mail **and** opening it                      |
| **Rebase**      | Re-stacking your letters on top of new letters        |
| **Merge**       | Combining two piles of letters side by side           |
| **Push**        | Mailing your sealed letters back to headquarters      |

***

## Basic Commands


Think of your terminal as the mailroom window—you hand over commands, and Git processes them.

```bash
# 1. See whats changed on your desk

git status

# 2. Choose letters to mail

git add file.md

# 3. Seal and label them

git commit -m "docs: clarify Git workflow"

# 4. Peek at the post office (get new mail)

git fetch origin

# 5. Re-stack your letters on top of the newest mail

git rebase origin/main

# 6. Send your sealed letters back

git push origin main
```

> 📋 **Example:** You’ve fixed a typo in `README.md`.
>
> ```bash
> git add README.md
> git commit -m "docs: fix typo in installation instructions"
> ```

***

## Daily Workflow


1. **Work locally.** Edit files in your editor—like drafting a letter at home.
2.  **Stage & commit.**

    ```bash
    git add .
    git commit -m "docs: update troubleshooting tips"
    ```

    _Think: “I’m sealing today’s changes.”_
3.  **Sync with the post office.**

    ```bash
    git fetch origin
    git rebase origin/main
    ```

    _Analogy: “Let me sort my letters on top of any new mail.”_
4.  **Push back.**

    ```bash
    git push origin main
    ```

    _Your letters arrive safely at GitHub._

> 💬 **Tip:** If `git push` is rejected, you probably need to fetch & rebase again first.

***

## Rebase vs. Merge


| Aspect         | Merge                                    | Rebase                                      |    |                                          |
| -------------- | ---------------------------------------- | ------------------------------------------- | -- | ---------------------------------------- |
| **History**    | Shows a side-by-side merge commit (“     |                                             | ”) | Keeps a single, straight line of commits |
| **Reads like** | “Here’s where I joined two roads.”       | “All the steps happened one after another.” |    |                                          |
| **Use when**   | You want a clear record of branch merges | You prefer a tidy, linear story             |    |                                          |
| **Analogy**    | Splicing two film reels together         | Splicing scenes onto the end of one reel    |    |                                          |

> ⚠️ **Warning:** Rebasing rewrites “history.” Never rebase commits others have already pulled.

***

## Handling Conflicts


When two cooks follow the same recipe and change the same line, you get a conflict:

```diff
<<<<<<< HEAD
Your version of the recipe
=======
Their version from the remote
>>>>>>> origin/main
```

**Steps to resolve:**

1. Open the file.
2. Decide which “ingredient” to keep.
3. Remove the `<<<<<<<`, `=======`, and `>>>>>>>` lines.
4.  Stage and continue:

    ```bash
    git add conflicted-file.md
    git rebase --continue
    ```
5. Repeat if needed.

> 🍴 **Analogy:** It’s like two chefs arguing over salt vs. pepper—pick one, or mix both politely.

***

## Best Practices


*   **Fetch before you start**

    ```bash
    git fetch origin && git rebase origin/main
    ```

    _Ensure you’re working on the latest version._
* **Keep commits focused.** One typo fix per commit, one feature per commit.
*   **Use branches** for big changes:

    ```bash
    git checkout -b feature/add-git-guide
    ```

    _Branch = a safe playground._
*   **Review before you push**:

    ```bash
    git diff origin/main
    ```

    _Spot anything odd._
* **Write clear messages**:
  * `feat:` for new content
  * `fix:` for corrections
  * `docs:` for documentation changes

***

## Troubleshooting


### “! \[rejected] main → main (fetch first)”


```bash
git fetch origin
git rebase origin/main
git push origin main
```

### “error: cannot pull with rebase: You have unstaged changes.”


Options:

*   **Commit** your changes:

    ```bash
    git add .
    git commit -m "wip: save progress"
    git pull --rebase
    ```
*   **Stash** them:

    ```bash
    git stash
    git pull --rebase
    git stash pop
    ```

    _Stash = a coat pocket for changes._

> ⚠️ **Note:** `git stash pop` can also conflict—resolve like any other conflict.

***

## Glossary


* **Fast-forward**: Your branch just moves ahead—no new commit needed.
* **Merge commit**: A special commit that ties two roads together.
* **Detached HEAD**: You’re exploring past commits without being on a branch—make a new branch before committing.
* **Force-push (`--force-with-lease`)**: Overwrites history carefully—use sparingly.

> 🏁 You’re all set to pull, rebase, and push confidently. Remember: Git is here to protect your work, not to trip you up.
