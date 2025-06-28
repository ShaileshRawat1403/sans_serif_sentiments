# ImmutableInk User Guide

## Table of Contents
* [How to Use This Guide](#how-to-use-this-guide)
* [Overview (Welcome to ImmutableInk)](#overview-welcome-to-immutableink)
    * [What is ImmutableInk?](#what-is-immutableink)
    * [Key Capabilities at a Glance](#key-capabilities-at-a-glance)
    * [Problems Immutable Ink Solves](#problems-immutable-ink-solves)
* [Understanding User Roles](#understanding-user-roles)
* [Getting Started with ImmutableInk](#getting-started-with-immutableink)
    * [System Requirements](#system-requirements)
    * [Account Setup](#account-setup)
    * [Your First Document](#your-first-document)
    * [Assign Reviewers](#assign-reviewers)
    * [Seal the Document](#seal-the-document)
    * [Verify Integrity](#verify-integrity)
    * [Share and Download](#share-and-download)
* [Quickstart Tutorial](#quickstart-tutorial)
    * [What You'll Need](#what-youll-need)
    * [What You'll Accomplish](#what-youll-accomplish)
    * [Procedure for a Complete Document Lifecycle](#procedure-for-a-complete-document-lifecycle)
        * [Create a New Document](#create-a-new-document)
        * [Submit for Review](#submit-for-review)
        * [Approve as a Reviewer](#approve-as-a-reviewer)
        * [Seal the Document](#seal-the-document-1)
        * [Verify Document Integrity](#verify-document-integrity-1)
* [Beyond Your First Document](#beyond-your-first-document)
    * [Manage Documents](#manage-documents)
    * [Explore Version History](#explore-version-history)
    * [Work with Templates](#work-with-templates)
    * [Integrate and Extend](#integrate-and-extend)
* [Troubleshooting Common Issues](#troubleshooting-common-issues)
    * [Login and Account Access Problems](#login-and-account-access-problems)
    * [Document Creation and Upload Challenges](#document-creation-and-upload-challenges)
    * [Review and Workflow Issues](#review-and-workflow-issues)
    * [Sealing and Verification Problems](#sealing-and-verification-problems)
    * [General System Behavior](#general-system-behavior)
    * [When to Contact Support](#when-to-contact-support)
* [Security Tips](#security-tips)
* [Accessibility](#accessibility)
* [What's New](#whats-new)
* [Key Terms](#key-terms)

---

### How to Use This Guide

Welcome to the ImmutableInk User Guide. This document provides essential information to help you understand, get started with, and effectively use the ImmutableInk platform.

**Navigating This Guide:**
Use the **Table of Contents** at the beginning of this document to quickly jump to specific sections.

**Conventions Used:**

* **Bold text:** Indicates user interface elements (buttons, menu items, field names) or important terms defined in the [Key Terms](#key-terms) section.

* `Code blocks`: Represent conceptual diagrams or simplified representations for clarity.

* ✅, ❌, ⚠️: Used as quick visual indicators for status or outcome.

**Provide Feedback:**
Your feedback helps us improve this documentation. If you have suggestions or find areas that need more clarity, please use the feedback mechanism provided on the ImmutableInk website, or contact our support team.

---

### Overview (Welcome to ImmutableInk)

This section provides a high-level introduction to ImmutableInk, outlining its purpose, core features, and the problems it addresses.

#### What is ImmutableInk?

ImmutableInk is a **blockchain-backed documentation platform** designed for verifiable, auditable, and tamper-evident documentation. It protects high-stakes content, such as contracts, compliance policies, and intellectual property, from tampering, disputes, and version control issues. Unlike traditional document systems, ImmutableInk ensures every signature, timestamp, and review is permanently recorded on a secure, immutable ledger. Think of the blockchain here as a highly secure, unchangeable digital record book where every entry is timestamped and linked, ensuring transparency and trust.

**Conceptual Diagram: ImmutableInk Document Lifecycle**

```

[Create Document] --(Submit for Review)--\> [In Review] --(Approve)--\> [Ready to Seal] --(Seal)--\> [Sealed on Blockchain]
|
v
[Verify Integrity]

```

*This diagram illustrates the core flow of a document from creation to a sealed and verifiable state within ImmutableInk.*

#### Key Capabilities at a Glance

ImmutableInk offers the following key capabilities:

* **Sealing:** Finalizes and cryptographically locks a document. This creates an unchangeable record on the blockchain.

* **Reviewer Chain:** Creates a cryptographically linked chain of approvals for audit and compliance. Each approval is permanently recorded.

* **Verify Integrity:** Matches a document's current digital fingerprint (hash) against its officially sealed version. This quickly detects any unauthorized changes.

* **Immutable Ledger:** Provides a permanent, blockchain-based history with time-stamped blocks. This ledger acts as an irrefutable audit trail.

* **Templates:** Offers pre-built structures for standard content (SOPs, Contracts, etc.) to streamline document creation.

* **API & Webhooks:** For technical users and system integrators, these tools automate verification, send alerts on events, and connect ImmutableInk to other business applications.

#### Problems Immutable Ink Solves

ImmutableInk provides solutions for common documentation challenges by:

* **Automated Logging:** Eliminating audit pain through provable, unchangeable records.

* **Clear Version States:** Resolving version confusion with definitive, sealed document states.

* **Provable Recording:** Preventing IP theft by proving document existence and state at any given time.

* **Tamper Detection:** Protecting against insider tampering with real-time detection and alerts.

### Understanding User Roles

ImmutableInk supports various user roles, each with specific permissions and responsibilities designed to streamline the document lifecycle. The following table provides a quick overview of each role:

| **Role** | **Key Responsibilities** |
| :------------------------ | :----------------------------------------------------------------------------------------------------------------- |
| **Writer** | Creates new documents, drafts content, and initiates the review process. Manages documents until they are sealed. |
| **Reviewer** | Accesses and reviews documents, suggests edits, adds comments, and provides approval or rejection based on content. |
| **Compliance Lead** | Oversees document reviews, ensures all approvals are gathered, and is responsible for sealing documents onto the immutable ledger. Holds final approval authority. |
| **Administrator** | Manages user accounts, assigns roles, configures workspace settings, and oversees system-level functionalities. |
| **Developer / System Integrator** | Utilizes ImmutableInk's API and webhooks to build custom integrations and extend platform functionality. |

### Getting Started with ImmutableInk

This section guides you through the onboarding process and your first steps in the system. Our goal is a frictionless experience to help you get your first document reviewed, sealed, and verified without requiring prior blockchain expertise.

#### System Requirements

To ensure the best experience with ImmutableInk, verify your system meets these requirements:

* **Browser:** Latest version of Chrome, Firefox, Safari, or Edge.

* **Account Types Supported:** Email/password OR Web3 wallet (MetaMask, Ledger, etc.).

* **Roles Available:** Writer, Reviewer, Compliance Lead. (Administrator and Developer roles are also available; these are typically for system setup and integration. Refer to the [Administrator Guide](#) for deployment and initial configuration details.)

* **Recommended Resolution:** 1440x900 pixels or above for optimal display.

#### Account Setup

Follow these steps to set up your ImmutableInk account:

1.  Visit the ImmutableInk **signup page**.

2.  Choose your sign-in method: **Email + password** OR connect your **Web3 Wallet**.

3.  Select your primary role (for example, **Writer** or **Reviewer**).

4.  Set up your workspace: Provide a name and invite your teammates to join.

#### Your First Document

You have two options for creating your first document:

* **Option A: Upload an Existing Document:** ImmutableInk supports **.docx, .md, .txt,** and **.pdf** formats. The system automatically creates a digital fingerprint (hash) of your document upon upload.

* **Option B: Start from Scratch:** Use the built-in **WYSIWYG** or **Markdown editor**. Auto-save is enabled to prevent loss of work.

#### Assign Reviewers

Once your document is ready for review, click "**Assign Reviewers**" (located on the right sidebar). You can choose between a **sequential** (reviewers approve one after the other) or **parallel** (all reviewers can approve simultaneously) review process.

#### Seal the Document

After all assigned reviews are complete, the user with the **Compliance Lead** role clicks "**Seal & Verify**." ImmutableInk then creates the final digital fingerprint (hash), securely locks the document's metadata and all associated signatures into a blockchain block, and updates the document status to **Sealed**.

#### Verify Integrity

Any authorized user can click "**Verify Integrity**" to compare the live document's current digital fingerprint with its officially sealed version on the blockchain. Status indicators will show:

* ✅ **Verified:** The document's current state matches its sealed, immutable record.

* ❌ **Modified / Tampered:** The document has been altered since it was last sealed.

* ⚠️ **Not Sealed:** The document has not yet been sealed to the blockchain.

**Visual: Understanding Document Integrity Status**

*This visual conceptually represents the outcome of an integrity check, helping users quickly understand the different statuses.*

```

\+------------------+     +------------------+     +------------------+
|                  |     |                  |     |                  |
|  ✅ VERIFIED     |     |  ❌ MODIFIED     |     |  ⚠️ NOT SEALED   |
|  Current Hash    |     |  Current Hash    |     |                  |
|  Matches Sealed  |     |  Does NOT Match  |     | Document has no  |
|  Hash            |     |  Sealed Hash     |     | immutable record |
|                  |     |                  |     |                  |
\+------------------+     +------------------+     +------------------+

```

#### Share and Download

ImmutableInk offers various ways to share and download your documents:

* Share via **permissioned links**, controlling who can view or verify the document.

* Embed a **QR Badge** directly into your physical documents for easy digital validation.

* Export an **Audit Mode PDF** which includes the document's digital fingerprint (hash), the complete reviewer chain, and all relevant timestamps for compliance purposes.

### Quickstart Tutorial

This hands-on tutorial guides you through the core ImmutableInk workflow, allowing you to create, review, and verify a document in approximately 10 minutes. The steps are numbered for clear procedural guidance.

#### What You'll Need

* An active ImmutableInk user account with the **Writer** role.

* The names of at least two other team members to act as **Reviewer** and **Compliance Lead**. (For the tutorial, you can assign these roles to yourself if you have administrator privileges.)

#### What You'll Accomplish

By completing this tutorial, you will:

1.  Create a new document.

2.  Submit the document for review.

3.  Approve the document as a reviewer.

4.  Seal the document as a compliance lead.

5.  Verify the integrity of the final, sealed document.

#### Procedure for a Complete Document Lifecycle

#### Create a New Document

1.  Log in to your ImmutableInk workspace.

2.  From your dashboard, click the "**+ New Document**" button in the top right corner and select "**Create from Scratch**".

3.  For the title, enter "Test Procedure - Q2 Safety Protocol" (or a similar descriptive title).

4.  In the editor body, type a few sentences of placeholder text (for example, "Begin your document by outlining the core steps of your safety protocol.").

5.  Click "**Save Draft**." The document status will now change to "**Draft**".

#### Submit for Review

1.  In the right-hand sidebar of your document, locate the "**Reviewers**" panel.

2.  Click "**Assign Reviewers**".

3.  Type the name of the user you want to act as a Reviewer and select them. Add a second user who will act as the Compliance Lead.

4.  Click "**Start Review**." The document status will change from "**Draft**" to "**In Review**," and the document will be locked from further editing.

#### Approve as a Reviewer

1.  If you assigned yourself as the reviewer, navigate back to your dashboard and open the document.

2.  Click the green "**Approve**" button at the top of the page.

3.  Confirm the action in the dialog box. Your approval is now recorded in the Reviewer Chain.

#### Seal the Document

1.  As the user designated Compliance Lead, open the document. The "**Approve**" button will now be replaced with a blue "**Seal Document**" button.

2.  Click "**Seal Document**." This action is final and signifies that the document is now the official version. Confirm the action.

3.  The document's status will change to "**Sealed**," indicated by a blue lock icon.

#### Verify Document Integrity

1.  With the sealed document open, locate and click the "**Verify Integrity**" button in the top bar.

2.  A verification panel will slide out, displaying a "**Verified**" status, matching hashes (Current Hash and Sealed Hash), and the complete Reviewer Chain.

3.  Congratulations! You have successfully created and verified your first document in ImmutableInk.

### Beyond Your First Document

Now that you've successfully created, reviewed, sealed, and verified your first document, explore these features to maximize your use of ImmutableInk.

#### Manage Documents

Easily access and organize all your documents from the ImmutableInk dashboard:

* **Search and Filter:** Use the search bar and filter options to quickly locate specific documents by title, status, or keywords.

* **Sort:** Sort documents by creation date, last modification date, or status to prioritize your work.

* **Archive:** Archive older or less frequently accessed documents to keep your active workspace organized.

#### Explore Version History

ImmutableInk maintains a robust version history for each document, providing a transparent audit trail:

* **View Past Versions:** Access previous sealed versions of your document to see its evolution over time.

* **Timestamping:** Each sealed version includes a precise timestamp, ensuring an undeniable record of when changes occurred.

* **Rollback Capability:** If needed, you can revert to a previous sealed version, making it the current working document for new revisions.

**Conceptual Chart: Document Version History Timeline**

*This chart illustrates how sealed versions of a document create a linear history, with each point representing an immutable record.*

```

Version 1.0 (Sealed:YYYY-MM-DD)
|
V
Version 1.1 (Sealed:YYYY-MM-DD)
|
V
Version 1.2 (Sealed:YYYY-MM-DD)
|
V
(Current Working Draft)

```

#### Work with Templates

Streamline your document creation process and ensure consistency across your organization using templates:

* **Create from Template:** When creating a new document, select from a library of pre-built templates (e.g., SOPs, Contracts, Meeting Minutes).

* **Custom Templates:** If you have administrator privileges, you can create and manage custom templates tailored to your organization's specific needs.

#### Integrate and Extend

ImmutableInk offers powerful integration capabilities to connect with your existing systems and automate workflows:

* **API (Application Programming Interface):** Developers can use ImmutableInk's API to programmatically interact with documents, trigger sealing, fetch verification data, and more.

* **Webhooks:** Set up webhooks to receive automated notifications when specific document events occur (e.g., a document is sealed, a review is completed), enabling real-time reactions in your connected applications.

* For detailed technical documentation on integrating with ImmutableInk, refer to our [Developer Documentation Portal](#). (Note: This is a placeholder link, replace with actual link if available).

### Troubleshooting Common Issues

When you're getting started with any new software, encountering a snag can be frustrating. This section aims to help you quickly resolve the most common issues you might face while using ImmutableInk, ensuring a smooth experience.

#### Login and Account Access Problems

* **Issue: Cannot log in, "Invalid credentials" error.**

    * **Solution:** Double-check your username (email address) and password. Passwords are case-sensitive.

    * **Action:** If you've forgotten your password, use the "**Forgot Password?**" link on the login page to reset it.

    * **Check:** Ensure there are no extra spaces before or after your email address.

* **Issue: Web3 Wallet (for example, MetaMask) is not connecting or showing.**

    * **Solution:**

        1.  Ensure your Web3 wallet extension is installed and active in your browser.

        2.  Check that your wallet is unlocked and connected to the correct network (if applicable, ImmutableInk typically operates on a specific public blockchain or a private network).

        3.  Refresh the ImmutableInk login page.

        4.  Verify that your browser extensions are not interfering (try temporarily disabling others if issues persist).

    * **Check:** Does your wallet have an active account selected?

* **Issue: Account locked or suspended.**

    * **Solution:** If you attempt too many failed logins, your account might be temporarily locked for security. Wait for the specified lockout period (usually 15-30 minutes) and try again.

    * **Action:** If the issue persists, contact your organization's ImmutableInk administrator or ImmutableInk Support immediately.

#### Document Creation and Upload Challenges

* **Issue: Document upload fails or shows an error.**

    * **Solution:**

        1.  **Supported Formats:** Ensure your document is in a supported format (**.docx, .md, .txt, .pdf**). Other formats will not upload.

        2.  **File Size:** Check the file size. Extremely large documents might take longer or exceed upload limits (refer to your plan's specific limits or contact support).

        3.  **Internet Connection:** Verify your internet connection is stable.

        4.  **Browser Cache:** Clear your browser's cache and cookies, then try uploading again.

    * **Check:** Does the file name contain any unusual characters? Try renaming it to something simple (e.g., `document.docx`).

* **Issue: Editor is slow or unresponsive.**

    * **Solution:**

        1.  **Browser Performance:** Close other demanding browser tabs or applications.

        2.  **Internet Connection:** A slow internet connection can affect editor responsiveness, especially for large documents.

        3.  **Browser Updates:** Ensure your web browser is updated to the latest version.

        4.  **Restart Browser:** Close and reopen your browser.

    * **Check:** Does the issue occur in a different browser?

#### Review and Workflow Issues

* **Issue: Reviewer did not receive a notification.**

    * **Solution:**

        1.  **Spam Folder:** Ask the reviewer to check their email's spam or junk folder.

        2.  **Email Address:** Verify that the correct email address was entered when assigning the reviewer.

        3.  **ImmutableInk Notifications:** Ensure the reviewer's ImmutableInk notification settings are not disabled.

        4.  **Administrator Check:** If your organization uses an allowlist for emails, ensure ImmutableInk's notification emails are permitted.

    * **Action:** You can resend the review request from the document's review panel if available.

* **Issue: Document is stuck "In Review" or cannot be approved.**

    * **Solution:**

        1.  **All Approvals:** Check if all assigned reviewers have completed their approval steps. A document cannot proceed until all required approvals are in.

        2.  **Correct Role:** Ensure the user attempting to approve has the necessary "**Reviewer**" or "**Compliance Lead**" role for that specific step.

        3.  **Sequential Review:** If your review process is sequential, ensure the current step's reviewer has completed their action before the next reviewer can act.

    * **Check:** Is there an active network issue preventing the approval action from registering?

#### Sealing and Verification Problems

* **Issue: Cannot "Seal Document" button is not active.**

    * **Solution:**

        1.  **Review Completion:** The document must have successfully completed all assigned review stages. The button will remain inactive until all approvals are in.

        2.  **Compliance Lead Role:** Only users with the "**Compliance Lead**" role (or equivalent administrator privileges) can seal a document. Verify your assigned role.

    * **Check:** Has the document's status visibly changed from "**In Review**" to "**Ready to Seal**"?

* **Issue: "Verify Integrity" shows "Modified / Tampered" or "Not Sealed."**

    * **Solution:**

        1.  **Modified / Tampered:** This indicates that the live document's content has changed *after* it was sealed. If this was an intentional edit, the document needs to be re-sealed to create a new immutable record. If unintentional, this flags a critical integrity breach.

        2.  **Not Sealed:** The document has not yet been sealed. Only sealed documents can be verified against an immutable record. Proceed with the sealing process (ensure all reviews are complete and you have the Compliance Lead role).

    * **Action:** If a tampering alert is unexpected, immediately investigate the source of the modification.

#### General System Behavior

* **Issue: Pages load slowly or the application feels sluggish.**

    * **Solution:**

        1.  **Internet Connection:** Test your internet speed. A poor connection is the most common cause.

        2.  **Browser Issues:** Try clearing your browser's cache and cookies. Ensure your browser is up-to-date.

        3.  **System Resources:** Close other demanding browser tabs or applications.

        4.  **Network Firewall:** If you are on a corporate network, a firewall might be restricting access. Consult your IT department.

    * **Check:** Does the issue persist if you try accessing ImmutableInk from a different device or network?

#### When to Contact Support

If you've tried the troubleshooting steps above and are still experiencing issues, or if you encounter an error message not listed here, please contact your organization's ImmutableInk administrator or ImmutableInk Support with the following information:

* **Your User Role:** (e.g., Writer, Reviewer, Admin)

* **The Exact Problem:** Describe what you are trying to do and what happens.

* **Any Error Messages:** Provide the full text of any error messages.

* **Steps to Reproduce:** List the steps you took leading up to the issue.

* **Browser and Operating System:** (e.g., Chrome 120 on Windows 11)

* **Date and Time:** When the issue occurred.

Providing this detail will help your support team resolve your issue quickly and efficiently.

### Security Tips

ImmutableInk leverages advanced cryptographic principles for document integrity. To ensure the highest level of security for your account and documents, consider these best practices:

* **Strong Passwords:** Always use strong, unique passwords for your ImmutableInk account. Combine uppercase and lowercase letters, numbers, and symbols.

* **Multi-Factor Authentication (MFA):** Enable MFA if available for an extra layer of security on your account.

* **Web3 Wallet Security:** If using a Web3 wallet, keep your recovery phrase (seed phrase) safe and never share it. Use hardware wallets for enhanced security where possible.

* **Phishing Awareness:** Be vigilant against phishing attempts. Always verify the URL before entering your credentials or connecting your wallet.

* **Regular Updates:** Keep your web browser and operating system updated to benefit from the latest security patches.

### Accessibility

ImmutableInk is committed to providing an accessible experience for all users. We strive to meet industry standards for web accessibility to ensure our platform is usable by individuals with diverse needs.

* **Keyboard Navigation:** All core functionalities are navigable using only a keyboard.

* **Screen Reader Compatibility:** The user interface is designed to be compatible with popular screen readers, providing appropriate semantic structure and alternative text.

* **Color Contrast:** We aim for sufficient color contrast to ensure readability for users with low vision or color blindness.

We continuously work to improve accessibility. If you encounter any accessibility barriers or have suggestions, please contact our support team.

### What's New

Stay up-to-date with the latest features, enhancements, and bug fixes in ImmutableInk. We regularly release updates to improve your experience and expand the platform's capabilities.

* **In-App Notifications:** Look for in-app notifications on your dashboard for immediate updates.

* **Release Notes:** For a detailed list of all changes, features, and improvements in each version, please refer to our official Release Notes documentation on the ImmutableInk website. (Note: This is a placeholder link, replace with actual link if available).

### Key Terms

This glossary provides definitions for key terms used throughout the ImmutableInk User Guide:

* **Blockchain:** A decentralized, distributed digital ledger that records transactions (in our case, document states and approvals) across many computers. It is designed to be immutable, meaning once data is added, it cannot be altered.

* **Cryptographic Hashing:** A mathematical algorithm that takes an input (e.g., a document) and produces a fixed-size string of characters, called a "hash" or "digital fingerprint." Even a tiny change to the input will result in a completely different hash.

* **Immutable Ledger:** The permanent, unchangeable record of all sealed documents and their associated metadata on the blockchain. This ledger provides irrefutable proof of a document's state at a specific time.

* **Non-Repudiation:** A legal concept ensuring that a party to a contract or communication cannot deny the authenticity of their signature on a document, nor can they deny having sent a message that has been digitally signed. ImmutableInk's digital signatures contribute to non-repudiation.

* **Reviewer Chain:** A chronological and cryptographically secured record of all approvals and rejections for a document, providing a clear audit trail.

* **Sealing:** The process of finalizing a document's current state and recording its unique digital fingerprint (hash) and other relevant metadata onto the blockchain, making it tamper-evident and immutable.

* **Web3 Wallet:** A software application or hardware device that allows users to interact with blockchain networks, manage cryptocurrency, and securely sign transactions (such as document approvals or seals in ImmutableInk).
