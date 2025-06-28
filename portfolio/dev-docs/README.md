# ImmutableInk Developer Guide

## Table of Contents
* [Introduction](#introduction-anchor)
* [Getting Started for Developers](#getting-started-developers-anchor)
    * [Prerequisites](#prerequisites-dev-anchor)
    * [Authentication](#authentication-dev-anchor)
    * [Make Your First API Call](#first-api-call-anchor)
* [Core Concepts for Developers](#core-concepts-dev-anchor)
    * [ImmutableInk Architecture Overview](#architecture-overview-anchor)
    * [Understanding Hashes and Signatures](#hashes-signatures-anchor)
    * [Data Models](#data-models-anchor)
* [API Reference](#api-reference-anchor)
    * [Documents API](#documents-api-anchor)
        * [Create a Document](#create-document-api-anchor)
        * [Get Document Details](#get-document-details-api-anchor)
        * [Update Document Content](#update-document-content-api-anchor)
        * [Submit for Review](#submit-for-review-api-anchor)
        * [Seal a Document](#seal-document-api-anchor)
        * [Verify Document Integrity](#verify-document-integrity-api-anchor)
    * [Reviews API](#reviews-api-anchor)
        * [Approve a Review](#approve-review-api-anchor)
        * [Reject a Review](#reject-review-api-anchor)
    * [Users API (Read-Only)](#users-api-anchor)
* [Webhooks](#webhooks-anchor)
    * [Register a Webhook Endpoint](#register-webhook-anchor)
    * [Event Types](#event-types-webhook-anchor)
    * [Webhook Payload Structure](#webhook-payload-anchor)
    * [Verify Webhook Signatures](#verify-webhook-signatures-anchor)
* [Error Codes and Handling](#error-codes-anchor)
* [Rate Limiting](#rate-limiting-anchor)
* [SDKs and Libraries](#sdks-libraries-anchor)
* [Best Practices for Integration](#best-practices-integration-anchor)
* [Related Documentation](#related-docs-dev-anchor)
* [Key Terms (Developer)](#key-terms-dev-anchor)

---

<a name="introduction-anchor"></a>
### Introduction

This guide provides comprehensive information for developers and system integrators who wish to interact with ImmutableInk programmatically. Learn how to leverage ImmutableInk's API and webhooks to integrate with your existing applications, automate document workflows, and build custom solutions.

---

<a name="getting-started-developers-anchor"></a>
### Getting Started for Developers

Begin your integration journey with ImmutableInk by setting up your development environment and making your first API call.

<a name="prerequisites-dev-anchor"></a>
#### Prerequisites

Before you start, ensure you have:

* An ImmutableInk **Developer account** with API access enabled.
* An **API Key** generated from your ImmutableInk workspace settings.
* A basic understanding of **RESTful APIs** and **JSON**.
* A development environment with tools like `curl` or a programming language (e.g., Python, Node.js) capable of making HTTP requests.
* (Optional, for local development/testing): A local ImmutableInk instance running, potentially via Docker Compose as described in the [Installation Guide](#).

<a name="authentication-dev-anchor"></a>
#### Authentication

ImmutableInk API requests are authenticated using an API Key provided in the request headers.

1.  **Obtain your API Key:** Log in to your ImmutableInk workspace, navigate to **Settings** > **API Access**, and generate a new API Key.
2.  **Include in Headers:** Pass your API Key in the `Authorization` header with the `Bearer` scheme for every request:

    `Authorization: Bearer YOUR_API_KEY`

*Keep your API Key confidential and secure. Do not expose it in client-side code.*

<a name="first-api-call-anchor"></a>
#### Make Your First API Call

Test your setup by retrieving a list of your accessible documents.

**Request:**
```http
GET /api/v1/documents
Authorization: Bearer YOUR_API_KEY
````

**Example using cURL:**

```bash
curl -X GET \
  [https://api.immutableink.com/api/v1/documents](https://api.immutableink.com/api/v1/documents) \
  -H 'Authorization: Bearer YOUR_API_KEY'
```

*Replace `YOUR_API_KEY` with your actual API Key.*

**Example Response (Success):**

```json
HTTP/1.1 200 OK
Content-Type: application/json

[
  {
    "id": "doc_abc123",
    "title": "Project Proposal Q3",
    "status": "sealed",
    "created_at": "2025-06-01T10:00:00Z",
    "updated_at": "2025-06-05T15:30:00Z",
    "owner_id": "user_123"
  },
  {
    "id": "doc_def456",
    "title": "HR Policy v2.0",
    "status": "in_review",
    "created_at": "2025-06-10T09:00:00Z",
    "updated_at": "2025-06-12T11:00:00Z",
    "owner_id": "user_456"
  }
]
```

*If you receive a `200 OK` response with a list of documents, your API setup is successful.*

-----

\<a name="core-concepts-dev-anchor"\>\</a\>

### Core Concepts for Developers

Understanding these fundamental concepts will help you effectively utilize the ImmutableInk API.

\<a name="architecture-overview-anchor"\>\</a\>

#### ImmutableInk Architecture Overview

ImmutableInk's architecture separates the user-facing application from the underlying blockchain integrity layer. The API acts as the primary interface for programmatic interaction with document creation, review, sealing, and verification. All integrity-related operations (hashing, signing, blockchain anchoring) are handled securely by the ImmutableInk backend services, abstracting the blockchain complexity from your integration.

**Simplified API Interaction Flow:**

```
[Your Application]
      | (API Call: Create Document)
      V
[ImmutableInk API Gateway]
      | (Internal Processing: Hashing, Blockchain Interaction)
      V
[ImmutableInk Core Services] <-- Writes to --> [Immutable Ledger (Blockchain)]
      | (API Response: Document ID, Status)
      V
[Your Application]
```

*This diagram illustrates how your application interacts with ImmutableInk's API, abstracting the blockchain layer.*

\<a name="understanding-hashes-signatures-anchor"\>\</a\>

#### Understanding Hashes and Signatures

  * **Document Hash:** Every version of a document submitted to ImmutableInk generates a unique cryptographic hash (a "digital fingerprint"). This hash changes if even a single character in the document content is altered.
  * **Digital Signatures:** When a document is sealed or reviewed, ImmutableInk securely associates digital signatures from the relevant users. These signatures are cryptographically linked to the document's hash and the blockchain record, providing non-repudiation.
  * **Integrity Verification:** The API provides endpoints to verify a document's integrity by re-hashing its current content and comparing it against the sealed hash on the blockchain.

\<a name="data-models-anchor"\>\</a\>

#### Data Models

ImmutableInk API uses standard JSON objects to represent resources. Key data models you will interact with include:

  * **Document Object:** Represents a document within ImmutableInk.
      * `id` (string): Unique identifier for the document.
      * `title` (string): Document title.
      * `status` (enum: `draft`, `in_review`, `ready_to_seal`, `sealed`): Current state of the document.
      * `content` (string): The raw content of the document (format depends on original upload, e.g., Markdown, plain text).
      * `owner_id` (string): ID of the user who owns the document.
      * `current_hash` (string, optional): SHA-256 hash of the current document content.
      * `sealed_hash` (string, optional): SHA-256 hash of the document when it was last sealed to the blockchain.
      * `created_at` (timestamp): Document creation time.
      * `updated_at` (timestamp): Last update time.
  * **Review Object:** Represents a review associated with a document.
      * `id` (string): Unique identifier for the review.
      * `document_id` (string): ID of the document being reviewed.
      * `reviewer_id` (string): ID of the user who is the reviewer.
      * `status` (enum: `pending`, `approved`, `rejected`): Current status of the review.
      * `comments` (string, optional): Reviewer comments.
  * **User Object:** Represents an ImmutableInk user.
      * `id` (string): Unique identifier for the user.
      * `email` (string): User's email address.
      * `role` (enum: `writer`, `reviewer`, `compliance_lead`, `administrator`, `developer`): User's assigned role.

-----

\<a name="api-reference-anchor"\>\</a\>

### API Reference

This section provides detailed specifications for ImmutableInk's REST API endpoints.

**Base URL:** `https://api.immutableink.com/api/v1` (Note: This is a placeholder, replace with actual base URL).

**Headers (Common):**

  * `Authorization: Bearer YOUR_API_KEY`
  * `Content-Type: application/json` (for POST/PUT requests with a body)

#### Documents API

Manage your ImmutableInk documents.

\<a name="create-document-api-anchor"\>\</a\>

##### Create a Document

`POST /documents`

Creates a new document in draft status.

**Request Body:**

```json
{
  "title": "My New Project Proposal",
  "content": "## Introduction\nThis is the content of my new document.",
  "format": "markdown" // or "text", "html"
}
```

**Responses:**

  * `201 Created`: Document successfully created.
    ```json
    {
      "id": "doc_new123",
      "title": "My New Project Proposal",
      "status": "draft",
      "owner_id": "user_xyz",
      "created_at": "2025-06-28T14:30:00Z"
    }
    ```
  * `400 Bad Request`: Invalid input.
  * `401 Unauthorized`: Missing or invalid API Key.

\<a name="get-document-details-api-anchor"\>\</a\>

##### Get Document Details

`GET /documents/{id}`

Retrieves the details of a specific document by its ID.

**Path Parameters:**

  * `id` (string, required): The unique identifier of the document.

**Responses:**

  * `200 OK`: Document details retrieved.
    ```json
    {
      "id": "doc_abc123",
      "title": "Project Proposal Q3",
      "status": "sealed",
      "content": "## Introduction\n...",
      "owner_id": "user_123",
      "sealed_hash": "a1b2c3d4e5f6...",
      "created_at": "2025-06-01T10:00:00Z"
    }
    ```
  * `401 Unauthorized`: Missing or invalid API Key.
  * `404 Not Found`: Document with the specified ID does not exist or you lack permission.

\<a name="update-document-content-api-anchor"\>\</a\>

##### Update Document Content

`PUT /documents/{id}`

Updates the title or content of an existing document. Only allowed if the document is in `draft` status.

**Path Parameters:**

  * `id` (string, required): The unique identifier of the document.

**Request Body:**

```json
{
  "title": "Updated Project Proposal Q3",
  "content": "## Introduction\nThis is the updated content.",
  "format": "markdown"
}
```

**Responses:**

  * `200 OK`: Document successfully updated.
    ```json
    {
      "id": "doc_abc123",
      "title": "Updated Project Proposal Q3",
      "status": "draft",
      "updated_at": "2025-06-28T15:00:00Z"
    }
    ```
  * `400 Bad Request`: Document not in `draft` status, or invalid input.
  * `401 Unauthorized`: Missing or invalid API Key.
  * `404 Not Found`: Document with the specified ID does not exist or you lack permission.

\<a name="submit-for-review-api-anchor"\>\</a\>

##### Submit for Review

`POST /documents/{id}/submit-for-review`

Submits a document for review. Requires the document to be in `draft` status.

**Path Parameters:**

  * `id` (string, required): The unique identifier of the document.

**Request Body:**

```json
{
  "reviewer_ids": ["user_reviewer1", "user_reviewer2"],
  "review_type": "sequential" // or "parallel"
}
```

**Responses:**

  * `200 OK`: Document submitted for review.
    ```json
    {
      "id": "doc_abc123",
      "status": "in_review"
    }
    ```
  * `400 Bad Request`: Document not in `draft` status, invalid reviewer IDs, or review type.
  * `401 Unauthorized`: Missing or invalid API Key.
  * `404 Not Found`: Document with the specified ID does not exist.

\<a name="seal-document-api-anchor"\>\</a\>

##### Seal a Document

`POST /documents/{id}/seal`

Seals a document on the blockchain. Requires the document to be in `ready_to_seal` status (all reviews completed).

**Path Parameters:**

  * `id` (string, required): The unique identifier of the document.

**Responses:**

  * `200 OK`: Document successfully sealed.
    ```json
    {
      "id": "doc_abc123",
      "status": "sealed",
      "sealed_hash": "new_a1b2c3d4e5f6...",
      "sealed_at": "2025-06-28T16:00:00Z"
    }
    ```
  * `400 Bad Request`: Document not in `ready_to_seal` status, or user lacks Compliance Lead role.
  * `401 Unauthorized`: Missing or invalid API Key.
  * `403 Forbidden`: User does not have permission to seal this document.
  * `404 Not Found`: Document with the specified ID does not exist.

\<a name="verify-document-integrity-api-anchor"\>\</a\>

##### Verify Document Integrity

`GET /documents/{id}/verify-integrity`

Verifies the integrity of a sealed document.

**Path Parameters:**

  * `id` (string, required): The unique identifier of the document.

**Responses:**

  * `200 OK`: Integrity check result.
    ````json
    {
      "document_id": "doc_abc123",
      "is_verified": true,
      "current_hash": "a1b2c3d4e5f6...",
      "sealed_hash": "a1b2c3d4e5f6...",
      "message": "Document integrity verified."
    }
    ```json
    // Example: Modified/Tampered
    {
      "document_id": "doc_abc123",
      "is_verified": false,
      "current_hash": "different_hash...",
      "sealed_hash": "a1b2c3d4e5f6...",
      "message": "Document content has been modified since last seal."
    }
    ````
  * `400 Bad Request`: Document not sealed.
  * `401 Unauthorized`: Missing or invalid API Key.
  * `404 Not Found`: Document with the specified ID does not exist.

#### Reviews API

Manage document reviews programmatically.

\<a name="approve-review-api-anchor"\>\</a\>

##### Approve a Review

`POST /reviews/{id}/approve`

Approves a specific review.

**Path Parameters:**

  * `id` (string, required): The unique identifier of the review.

**Request Body:**

```json
{
  "comments": "Content looks good, approved."
}
```

**Responses:**

  * `200 OK`: Review approved.
    ```json
    {
      "review_id": "review_123",
      "status": "approved",
      "document_status": "ready_to_seal" // or "in_review" if other reviews pending
    }
    ```
  * `400 Bad Request`: Review already completed, or user not the assigned reviewer.
  * `401 Unauthorized`: Missing or invalid API Key.
  * `404 Not Found`: Review with the specified ID does not exist.

\<a name="reject-review-api-anchor"\>\</a\>

##### Reject a Review

`POST /reviews/{id}/reject`

Rejects a specific review.

**Path Parameters:**

  * `id` (string, required): The unique identifier of the review.

**Request Body:**

```json
{
  "comments": "Content needs revision on section 3.2."
}
```

**Responses:**

  * `200 OK`: Review rejected.
    ```json
    {
      "review_id": "review_123",
      "status": "rejected",
      "document_status": "draft" // Document reverts to draft for revision
    }
    ```
  * `400 Bad Request`: Review already completed, or user not the assigned reviewer.
  * `401 Unauthorized`: Missing or invalid API Key.
  * `404 Not Found`: Review with the specified ID does not exist.

#### Users API (Read-Only)

Retrieve user information.

*Note: User creation and management are typically handled via the ImmutableInk Administration API or UI for security reasons.*

\<a name="users-api-anchor"\>\</a\>

##### Get User Details

`GET /users/{id}`

Retrieves the details of a specific user by their ID.

**Path Parameters:**

  * `id` (string, required): The unique identifier of the user.

**Responses:**

  * `200 OK`: User details retrieved.
    ```json
    {
      "id": "user_123",
      "email": "john.doe@example.com",
      "role": "writer",
      "created_at": "2024-01-01T08:00:00Z"
    }
    ```
  * `401 Unauthorized`: Missing or invalid API Key.
  * `404 Not Found`: User with the specified ID does not exist.

-----

\<a name="webhooks-anchor"\>\</a\>

### Webhooks

ImmutableInk webhooks enable you to receive real-time notifications about events in your ImmutableInk workspace directly in your applications.

\<a name="register-webhook-anchor"\>\</a\>

#### Register a Webhook Endpoint

`POST /webhooks`

Registers a new webhook endpoint to receive event notifications.

**Request Body:**

```json
{
  "url": "https://your-app.com/webhook-listener",
  "event_types": ["document.sealed", "document.review_completed", "document.tampered"],
  "secret": "your_webhook_secret" // Used to verify webhook payload authenticity
}
```

**Responses:**

  * `201 Created`: Webhook successfully registered.
    ```json
    {
      "id": "wh_abc123",
      "url": "https://your-app.com/webhook-listener",
      "event_types": ["document.sealed", "document.review_completed", "document.tampered"],
      "created_at": "2025-06-28T17:00:00Z"
    }
    ```
  * `400 Bad Request`: Invalid input.
  * `401 Unauthorized`: Missing or invalid API Key.

\<a name="event-types-webhook-anchor"\>\</a\>

#### Event Types

ImmutableInk sends notifications for the following event types:

  * `document.created`: A new document is created.
  * `document.updated`: A document's content or title is updated.
  * `document.submitted_for_review`: A document enters the review workflow.
  * `document.review_completed`: All pending reviews for a document are complete (document status changes to `ready_to_seal`).
  * `document.sealed`: A document is successfully sealed on the blockchain.
  * `document.tampered`: A document's integrity check reveals it has been modified after sealing.
  * `review.approved`: A specific review is approved.
  * `review.rejected`: A specific review is rejected.

\<a name="webhook-payload-anchor"\>\</a\>

#### Webhook Payload Structure

Webhook payloads are JSON objects containing details about the event. All payloads include:

  * `event_type` (string): The type of event that occurred (e.g., `document.sealed`).
  * `timestamp` (string): ISO 8601 timestamp of the event.
  * `data` (object): An object containing the relevant resource (e.g., a Document object for `document.*` events, a Review object for `review.*` events).

**Example `document.sealed` Payload:**

```json
{
  "event_type": "document.sealed",
  "timestamp": "2025-06-28T17:30:00Z",
  "data": {
    "id": "doc_abc123",
    "title": "Project Proposal Q3",
    "status": "sealed",
    "owner_id": "user_123",
    "sealed_hash": "new_a1b2c3d4e5f6...",
    "sealed_at": "2025-06-28T17:30:00Z"
  }
}
```

\<a name="verify-webhook-signatures-anchor"\>\</a\>

#### Verify Webhook Signatures

For security, ImmutableInk signs each webhook request with a secret you provide during webhook registration. You should verify this signature on your server to ensure the payload is authentic and has not been tampered with.

1.  ImmutableInk includes a `X-ImmutableInk-Signature` header in each webhook request.
2.  This signature is a HMAC-SHA256 hash of the raw request body, using your webhook secret as the key.
3.  On your server, compute the HMAC-SHA256 hash of the received raw request body using your secret.
4.  Compare your computed hash with the value in the `X-ImmutableInk-Signature` header. If they match, the payload is verified.

*Refer to the code samples in our [GitHub repository](https://www.google.com/search?q=%23) (Placeholder: Link to Developer GitHub repo with code samples) for examples of signature verification in various languages.*

-----

\<a name="error-codes-anchor"\>\</a\>

### Error Codes and Handling

ImmutableInk API uses standard HTTP status codes to indicate the success or failure of an API request. Detailed error information is provided in the JSON response body.

| HTTP Status Code | Description                                  | Common Cause                                                     |
| :--------------- | :------------------------------------------- | :--------------------------------------------------------------- |
| `200 OK`         | Success                                      | Request was successful.                                          |
| `201 Created`    | Resource Created                             | A new resource (e.g., document, webhook) was successfully created. |
| `400 Bad Request` | Invalid Input / Malformed Request            | Missing required parameters, invalid JSON format, or incorrect data types. |
| `401 Unauthorized` | Authentication Failed                        | Missing or invalid `Authorization` header/API Key.             |
| `403 Forbidden`  | Permission Denied                            | API Key is valid, but the authenticated user lacks permission for the requested action (e.g., non-Compliance Lead attempting to seal). |
| `404 Not Found`  | Resource Not Found                           | The requested resource (e.g., document ID, review ID) does not exist. |
| `429 Too Many Requests` | Rate Limit Exceeded                        | You have sent too many requests in a given amount of time. (See [Rate Limiting](https://www.google.com/search?q=%23rate-limiting-anchor)). |
| `500 Internal Server Error` | Unexpected Server Error                      | An unhandled error occurred on the ImmutableInk server. If this persists, contact support. |

**Example Error Response:**

```json
HTTP/1.1 400 Bad Request
Content-Type: application/json

{
  "code": "invalid_document_status",
  "message": "Document must be in 'draft' status to be updated.",
  "details": {
    "current_status": "in_review",
    "expected_status": "draft"
  }
}
```

-----

\<a name="rate-limiting-anchor"\>\</a\>

### Rate Limiting

To ensure fair usage and system stability, ImmutableInk API applies rate limits to requests.

  * **Default Limit:** 100 requests per minute per API Key.
  * **Exceeding Limit:** If you exceed the rate limit, API calls will return a `429 Too Many Requests` HTTP status code.
  * **Headers:** Look for `X-RateLimit-Limit`, `X-RateLimit-Remaining`, and `X-RateLimit-Reset` headers in the API responses to manage your request rate.

Implement exponential backoff or a token bucket algorithm in your client applications to handle rate limits gracefully.

-----

\<a name="sdks-libraries-anchor"\>\</a\>

### SDKs and Libraries

ImmutableInk provides official and community-contributed SDKs to simplify interaction with our API. These SDKs handle authentication, request signing, and response parsing, allowing you to focus on your application's logic.

  * **Python SDK:** [Link to Python SDK GitHub/documentation](https://www.google.com/search?q=%23) (Placeholder)
  * **Node.js SDK:** [Link to Node.js SDK GitHub/documentation](https://www.google.com/search?q=%23) (Placeholder)

-----

\<a name="best-practices-integration-anchor"\>\</a\>

### Best Practices for Integration

Follow these recommendations for robust and efficient integration with ImmutableInk:

  * **Error Handling:** Always implement comprehensive error handling for API responses, particularly for `4xx` and `5xx` status codes.
  * **Idempotency:** When making `POST` requests that might be retried (e.g., creating documents), ensure your logic handles potential duplicate submissions gracefully. ImmutableInk APIs are designed to be idempotent where appropriate.
  * **Asynchronous Processing (for Webhooks):** Process webhook payloads asynchronously to avoid timeouts on your webhook endpoint.
  * **Logging:** Implement detailed logging of API requests, responses, and webhook payloads for auditing and troubleshooting.
  * **Security:** Store your API keys securely. Avoid hardcoding them directly in your application code. Use environment variables or a secrets management service.
  * **Version Control:** Pin your API version to `v1` to avoid unexpected breaking changes in future API updates. Monitor release notes for API version deprecations or changes.

-----

\<a name="related-docs-dev-anchor"\>\</a\>

### Related Documentation

For more information on ImmutableInk:

  * [ImmutableInk User Guide](https://www.google.com/search?q=link-to-user-guide.md): Get started with the ImmutableInk web application.
  * [ImmutableInk Installation Guide](https://www.google.com/search?q=link-to-installation-guide.md): Deploy ImmutableInk in your environment.
  * [ImmutableInk Administration Guide](https://www.google.com/search?q=link-to-admin-guide.md): Manage your ImmutableInk instance, users, and security settings. (Placeholder)
  * [ImmutableInk Release Notes](https://www.google.com/search?q=link-to-release-notes.md): Stay updated on new features and improvements.

-----

\<a name="key-terms-dev-anchor"\>\</a\>

### Key Terms (Developer)

This glossary defines technical terms relevant to integrating with the ImmutableInk API:

  * **API (Application Programming Interface):** A set of rules and definitions that allows one software application to communicate with another.
  * **API Key:** A unique token used to authenticate requests to the ImmutableInk API, verifying the identity of the calling application or user.
  * **Endpoint:** A specific URL within an API that performs a particular function (e.g., `/api/v1/documents`).
  * **HTTP Status Code:** A three-digit number returned by a server in response to an HTTP request, indicating whether a particular HTTP request has been successfully completed.
  * **JSON (JavaScript Object Notation):** A lightweight data-interchange format that is human-readable and easily parsed by machines. Used for request and response bodies in the ImmutableInk API.
  * **Payload:** The data sent or received in an API request or webhook notification, typically in JSON format.
  * **Rate Limiting:** A control mechanism to limit the number of API requests a user or application can make within a given time frame to prevent abuse and ensure stability.
  * **RESTful API:** (Representational State Transfer) An architectural style for networked applications that relies on a stateless, client-server protocol (HTTP).
  * **SDK (Software Development Kit):** A collection of software development tools that allows the creation of applications for a certain software package, framework, hardware platform, computer system, video game console, operating system, or similar development platform.
  * **Webhook:** A method of augmenting or altering the behavior of a web page, or web application, with custom callbacks. Webhooks are user-defined HTTP callbacks.
