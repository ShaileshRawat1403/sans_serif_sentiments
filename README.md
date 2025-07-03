---
title: "Sans_Serif_Sentiments"
description: "An open-source Docs-as-Code portfolio showcasing CI/CD…"
tags: [docs-as-code, CI/CD, portfolio]
author: ShaileshRawat1403
last_updated: 2025-07-03
---

## Table of Contents

1. [About This Handbook](#about-this-handbook)
2. [Prerequisites](#prerequisites)
3. [What You’ll Learn](#what-youll-learn)
4. [Navigation](#navigation)
5. [Disclaimer](#disclaimer)

---

# Sans_Serif_Sentiments

> **Disclaimer:** This project is a personal experimentation in experiential learning—sharing what I’ve discovered about applying Git and CI/CD to documentation. It also serves as a portfolio showcase to demonstrate the power of Docs-as-Code and attract potential collaborators or employers.

Welcome to **Sans_Serif_Sentiments**, an open-source repository that illustrates how **CI/CD pipelines** and a **Docs-as-Code** approach can elevate *any* form of documentation—user guides, product docs, internal communications, marketing collateral, and more.

## Our Philosophy

- **Docs-as-Code**  
  Treat documentation like software: version it in Git, review via Pull Requests, and enforce quality through automated linters and checks.
- **CI/CD for Docs**  
  Every branch and PR triggers pipelines running markdown-lint, frontmatter validation, link-checking, and spell-check—keeping your docs accurate, complete, and production-ready.
- **Content Governance**  
  With structured frontmatter, tagged versions, and enforced templates:  
  - **Auditability:** track who changed what, when, and why  
  - **Traceability:** connect updates to issues or feature requests  
  - **Consistency:** apply style rules automatically across all files
- **Communication Robustness**  
  Whether for change management, customer manuals, or marketing playbooks:  
  - Enables coordinated, rapid updates  
  - Prevents stale or conflicting versions  
  - Scales governance across distributed teams
- **Open-Source Experimentation & Portfolio**  
  This is my journey in experiential learning—documenting pipelines and templates for writers—and a showcase of my work to demonstrate Git’s power for documentation and attract future opportunities.

## Pillars

| Directory                                                        | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| **[ai-handbook](ai-handbook/)**                                   | A human-centric guide to using generative AI thoughtfully.       |
| **[technical-communication-docs](technical-communication-docs/)** | Best practices for clear, concise technical writing.             |
| **[change-communication](change-communication/)**                 | Strategies and templates for effective organizational change.    |
| **[marcom-playbook](marcom-playbook/)**                           | Marketing communications resources, campaigns, and storytelling. |
| **[templates-workshop](templates-workshop/)**                     | Reusable Docs-as-Code templates, callout snippets, and toolkit.  |

## Getting Started

1. **Clone** the repo and switch to `main`  
   git clone https://github.com/ShaileshRawat1403/sans_serif_sentiments.git  
   cd sans_serif_sentiments  
   git checkout main
2. **Explore** a pillar by opening its `README.md` for module overviews and links.
3. **Contribute** on a feature branch  
   git checkout -b docs/your-change  
   # make edits…  
   git add .  
   git commit -m "docs: your change description"  
   git push -u origin docs/your-change
4. **Review & Merge** once CI checks pass, ensuring `main` remains stable.

## Contributing

Adopt our **branch-per-change** workflow:  
- `fix/...` – typos and minor tweaks  
- `docs/...` – content additions and proofreading  
- `chore/...` – scaffolding, CI config, renames  
- `feat/...` – new modules, major reorganizations

Pull requests enable peer review, automated validation, and transparent history for every change.

*Sans_Serif_Sentiments* is an evolving, open-source effort to empower writers with code-centric documentation practices—experiment, learn, and contribute to make documentation more robust, traceable, and collaborative!
