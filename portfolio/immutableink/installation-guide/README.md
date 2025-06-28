# ImmutableInk Installation Guide

## Table of Contents
* [Introduction](#introduction-anchor)
* [Deployment Options](#deployment-options-anchor)
* [Before You Begin: Prerequisites](#prerequisites-anchor)
    * [System Requirements](#system-requirements-install-anchor)
    * [Software Requirements](#software-requirements-anchor)
    * [Network Requirements](#network-requirements-anchor)
    * [Account and Permissions](#account-permissions-anchor)
* [Installation Procedure: Self-Hosted (Docker Compose)](#installation-docker-anchor)
    * [Step 1: Install Docker and Docker Compose](#install-docker-anchor)
    * [Step 2: Download ImmutableInk Deployment Files](#download-files-anchor)
    * [Step 3: Configure Environment Variables](#configure-env-anchor)
    * [Step 4: Start ImmutableInk Services](#start-services-anchor)
    * [Step 5: Complete Initial Setup](#initial-setup-anchor)
* [Verify Your Installation](#verify-installation-anchor)
* [Post-Installation Configuration](#post-install-config-anchor)
    * [Set Up Persistent Storage](#persistent-storage-anchor)
    * [Configure SSL/TLS](#configure-ssl-anchor)
    * [Integrate with Single Sign-On (SSO)](#integrate-sso-anchor)
    * [Implement Backup and Recovery](#backup-recovery-anchor)
    * [Update ImmutableInk](#update-immutableink-anchor)
* [Troubleshooting Installation Issues](#troubleshooting-install-anchor)
* [Related Documentation](#related-docs-install-anchor)
* [Key Terms (Installation)](#key-terms-install-anchor)

---

<a name="introduction-anchor"></a>
### Introduction

This guide provides comprehensive instructions for installing and setting up ImmutableInk. It targets system administrators and IT professionals responsible for deploying and configuring the software within their environment. By following these steps, you can successfully prepare your infrastructure and launch ImmutableInk.

---

<a name="deployment-options-anchor"></a>
### Deployment Options

ImmutableInk offers flexible deployment options to suit various organizational needs. This guide focuses on the **Self-Hosted Deployment using Docker Compose**, which provides a streamlined way to get ImmutableInk running in your environment.

Other deployment options, such as cloud-specific deployments (e.g., Kubernetes, AWS, Azure, GCP) or bare-metal enterprise installations, are covered in separate advanced administration guides.

---

<a name="prerequisites-anchor"></a>
### Before You Begin: Prerequisites

Before you start the installation, ensure your system meets all the necessary requirements. Fulfilling these prerequisites is critical for a smooth and successful deployment.

<a name="system-requirements-install-anchor"></a>
#### System Requirements

Verify your server or virtual machine meets the minimum hardware specifications:

* **Operating System:** Linux (Ubuntu 20.04+, RHEL 8+ recommended). Windows Server and macOS are supported for development/testing environments, but not recommended for production.
* **CPU:** 2 Cores (minimum), 4 Cores (recommended for production).
* **RAM:** 4 GB (minimum), 8 GB (recommended for production).
* **Disk Space:** 50 GB (minimum, for application and database data), 100 GB+ (recommended, depending on expected document volume). Ensure adequate IOPS (Input/Output Operations Per Second, a measure of disk read/write speed) for database operations.

<a name="software-requirements-anchor"></a>
#### Software Requirements

Install the following software on your deployment host:

* **Docker Engine:** Version 20.10.0 or higher.
* **Docker Compose:** Version 1.29.0 or higher (or Docker Compose V2).
* **Git:** For cloning the ImmutableInk deployment repository.
* **OpenSSL:** For generating SSL/TLS certificates (if you plan to use self-signed certificates initially).

<a name="network-requirements-anchor"></a>
#### Network Requirements

Configure your network to allow necessary communication:

* **Inbound Ports:**
    * **Port 80 (HTTP):** For initial access and redirection to HTTPS.
    * **Port 443 (HTTPS):** For secure web access to the ImmutableInk application.
    * **Internal Ports:** Ensure internal network communication between Docker containers is not blocked. Docker Compose manages this by default, so explicit internal firewall rules are usually not needed between ImmutableInk's containers.
* **Firewall Rules:** Configure firewall rules on your host and network devices to allow inbound traffic on ports 80 and 443 to your ImmutableInk server.
* **DNS Resolution:** Ensure your server can resolve external domain names and that your chosen ImmutableInk domain (if any) points to your server's public IP address.

<a name="account-permissions-anchor"></a>
#### Account and Permissions

Ensure you have the necessary account access and permissions:

* **Sudo/Root Access:** You must have `sudo` or root privileges on the deployment host to install Docker and manage services.
* **ImmutableInk Administrator Account:** Have details for an initial ImmutableInk administrator account (if provided separately by your vendor) or be prepared to create one during initial setup.

---

<a name="installation-docker-anchor"></a>
### Installation Procedure: Self-Hosted (Docker Compose)

Follow these steps to deploy ImmutableInk using Docker Compose. This procedure assumes you have met all [Prerequisites](#prerequisites-anchor).

<a name="install-docker-anchor"></a>
#### Step 1: Install Docker and Docker Compose

If you do not have Docker and Docker Compose installed, follow the official Docker documentation. These guides are specific to your Linux distribution's package manager (e.g., `apt` for Ubuntu, `yum` or `dnf` for RHEL/CentOS):

* **Install Docker Engine:** [Official Docker Engine Installation Guide](https://docs.docker.com/engine/install/) (Placeholder: Replace with actual link to Docker's official guide).
* **Install Docker Compose:** [Official Docker Compose Installation Guide](https://docs.docker.com/compose/install/) (Placeholder: Replace with actual link to Docker's official guide).

After installation, verify Docker is running and your user has permissions to run Docker commands without `sudo` (this is a common post-installation step in Docker guides).

```bash
docker --version
docker compose version
````

*Expected Output:*
`Docker version X.Y.Z, build ...`
`Docker Compose version vX.Y.Z`

\<a name="download-files-anchor"\>\</a\>

#### Step 2: Download ImmutableInk Deployment Files

Obtain the ImmutableInk Docker Compose deployment files. This typically involves cloning a Git repository:

```bash
git clone [https://github.com/immutableink/deployment.git](https://github.com/immutableink/deployment.git)
cd deployment
```

*This command clones the repository containing the necessary `docker-compose.yml` file and other configuration assets.*

\<a name="configure-env-anchor"\>\</a\>

#### Step 3: Configure Environment Variables

ImmutableInk uses environment variables for crucial settings. Create and edit a `.env` file in the `deployment` directory.

1.  **Create `.env` file:**

    ```bash
    cp .env.example .env
    ```

2.  **Edit `.env` file:** Open `.env` using a text editor (e.g., `nano .env` or `vim .env`). Configure at least the following:

      * `IMMUTABLEINK_DOMAIN=your.immutableink.com` (Replace with your chosen domain or server IP)
      * `DB_PASSWORD=your_secure_db_password` (Generate a strong password for your database)
      * `APP_SECRET_KEY=your_long_random_string` (Generate a long, random secret key for application security)
      * `ADMIN_EMAIL=admin@yourdomain.com` (Initial administrator email)
      * `ADMIN_PASSWORD=initial_admin_password` (Temporary password for initial login, **change immediately after first login**)

*Ensure these variables are correctly set, especially database credentials and secret keys, for both functionality and security.*

\<a name="start-services-anchor"\>\</a\>

#### Step 4: Start ImmutableInk Services

Use Docker Compose to build and start all ImmutableInk services in detached mode:

```bash
docker compose up -d --build
```

*This command downloads necessary Docker images, builds application services, and starts all containers defined in `docker-compose.yml` in the background.*

**Conceptual Chart: Docker Compose Service Architecture**

*This diagram illustrates how Docker Compose orchestrates different services (e.g., Web App, Database) for ImmutableInk.*

```
+---------------------+
|      Docker Host    |
| +-----------------+ |
| | Docker Engine   | |
| | +-------------+ | |
| | | Web App     |<---->| Database    |
| | | (Container) | | | (Container) | |
| | +-------------+ | | +-------------+ |
| |       ^         | |       ^         |
| |       |         | |       |         |
| |       v         | |       v         |
| | +-------------+ | | +-------------+ |
| | | Cache Svc   | | | | Worker Svc  | |
| | | (Container) | | | (Container) | |
| | +-------------+ | | +-------------+ |
| +-----------------+ |
+---------------------+
```

\<a name="initial-setup-anchor"\>\</a\>

#### Step 5: Complete Initial Setup

After services start, access ImmutableInk via your web browser to complete the initial setup:

1.  Open your web browser and navigate to `http://your.immutableink.com` (or your server's IP address if no domain is configured yet).
2.  Follow the on-screen prompts to finalize the application setup. This may include creating the initial admin user or confirming database migrations.
3.  Once prompted, log in with the **ADMIN\_EMAIL** and **ADMIN\_PASSWORD** you configured in the `.env` file.
4.  **Important:** Immediately change the `ADMIN_PASSWORD` through the ImmutableInk application settings after your first successful login for security.

-----

\<a name="verify-installation-anchor"\>\</a\>

### Verify Your Installation

After installation, confirm that all ImmutableInk services are running correctly and the application is accessible.

1.  **Check Docker Container Status:**

    ```bash
    docker compose ps
    ```

    *Expected Output:* All services (e.g., `web`, `db`, `worker`, `cache`) should show `Up` status.

2.  **View Application Logs (Optional):**

    ```bash
    docker compose logs -f
    ```

    *This command streams logs from all services, allowing you to monitor for errors or successful startup messages.*

3.  **Access the Web Interface:** Open your web browser and navigate to your ImmutableInk domain or server IP (e.g., `https://your.immutableink.com`). You should see the login screen.

-----

\<a name="post-install-config-anchor"\>\</a\>

### Post-Installation Configuration

After a successful initial installation, consider these crucial steps for a production-ready ImmutableInk deployment.

\<a name="set-up-persistent-storage-anchor"\>\</a\>

#### Set Up Persistent Storage

Ensure your database and application data persist even if containers are removed or recreated. This typically involves configuring Docker volumes for your database and application data directories. For example, ensure your `docker-compose.yml` mounts a volume for your database data (e.g., `db_data:/var/lib/postgresql/data`) and any application upload directories. Refer to the `docker-compose.yml` file and Docker documentation for detailed volume configuration.

\<a name="configure-ssl-anchor"\>\</a\>

#### Configure SSL/TLS

Secure your ImmutableInk instance with SSL/TLS certificates for HTTPS access.

**Important:** Ensure your domain's DNS records are correctly pointing to your server's public IP address *before* attempting to provision SSL/TLS certificates, especially with automated tools like Let's Encrypt.

  * **Option 1: Let's Encrypt (Recommended):** Use a tool like Certbot with your web server (e.g., Nginx, Caddy) to automate certificate issuance and renewal.
  * **Option 2: Custom Certificates:** Obtain certificates from a Certificate Authority (CA) and configure your web server to use them.

Refer to your web server's documentation and the [ImmutableInk Administration Guide](https://www.google.com/search?q=%23) (Placeholder: Link to Administration Guide) for detailed SSL/TLS setup.

\<a name="integrate-sso-anchor"\>\</a\>

#### Integrate with Single Sign-On (SSO)

For enhanced security and user management, integrate ImmutableInk with your organization's SSO provider (e.g., Okta, Azure AD, Google Workspace). Refer to the [ImmutableInk Administration Guide](https://www.google.com/search?q=%23) (Placeholder: Link to Administration Guide) for detailed SSO configuration steps and supported providers.

\<a name="implement-backup-recovery-anchor"\>\</a\>

#### Implement Backup and Recovery

Establish a robust backup strategy for your ImmutableInk data. This includes regular backups of your database (e.g., PostgreSQL data in the mounted volume) and any persistent application files (e.g., uploaded documents). Regularly test your recovery procedures to ensure data integrity.

\<a name="update-immutableink-anchor"\>\</a\>

#### Update ImmutableInk

Regularly update your ImmutableInk installation to benefit from new features, security patches, and performance improvements. Consult the [ImmutableInk Release Notes](https://www.google.com/search?q=%23) (Placeholder: Link to Release Notes) and the [Administrator Guide](https://www.google.com/search?q=%23) (Placeholder: Link to Administration Guide) for detailed update procedures.

-----

\<a name="troubleshooting-install-anchor"\>\</a\>

### Troubleshooting Installation Issues

This section provides solutions for common problems encountered during ImmutableInk installation.

  * **Issue: `docker compose up` fails with port conflicts.**

      * **Solution:** Another application on your server is already using ports 80 or 443.
      * **Action:**
        1.  Identify the conflicting process (e.g., `sudo netstat -tulpn | grep :80`).
        2.  Stop the conflicting process, or change the exposed ports in your `docker-compose.yml` file if direct access is not required.
        3.  Alternatively, use a reverse proxy (like Nginx or Caddy) to manage port forwarding, allowing multiple applications to share ports.

  * **Issue: Containers repeatedly stop or restart.**

      * **Solution:** This often indicates an issue with configuration (e.g., incorrect database credentials in `.env`) or a service dependency not starting correctly.
      * **Action:**
        1.  Check container logs for error messages: `docker compose logs` (use `-f` for live view). Error messages here are crucial for diagnosis.
        2.  Review your `.env` file for typos or incorrect values, especially passwords and secret keys.
        3.  Ensure your system meets [System Requirements](https://www.google.com/search?q=%23system-requirements-install-anchor) and has sufficient resources (RAM, CPU).

  * **Issue: Cannot access ImmutableInk in the browser (connection refused/timeout).**

      * **Solution:** This usually points to a network or firewall issue.
      * **Action:**
        1.  Verify ImmutableInk containers are `Up` using `docker compose ps`.
        2.  Check your server's firewall (e.g., `sudo ufw status` or `sudo firewall-cmd --list-all`) and ensure ports 80 and 443 are open.
        3.  Confirm your domain's DNS records correctly point to your server's public IP address.
        4.  Ensure no network proxies or VPNs are interfering with access.

  * **Issue: `git clone` fails.**

      * **Solution:** Network connectivity issues or incorrect repository URL.
      * **Action:**
        1.  Verify your server's internet connection (e.g., `ping google.com`).
        2.  Double-check the Git repository URL for typos.

-----

\<a name="related-docs-install-anchor"\>\</a\>

### Related Documentation

For more in-depth information on managing and extending ImmutableInk:

  * **ImmutableInk Administration Guide:** Comprehensive details on managing users, security, backups, and advanced configurations. (Placeholder: Link to actual Administration Guide).
  * **ImmutableInk Developer Documentation Portal:** Full API reference, SDKs, and guides for custom integrations. (Placeholder: Link to actual Developer Documentation Portal).
  * **ImmutableInk Release Notes:** Stay informed about product updates and changes. (Placeholder: Link to actual Release Notes).

-----

\<a name="key-terms-install-anchor"\>\</a\>

### Key Terms (Installation)

This glossary provides definitions for key terms specific to ImmutableInk installation and deployment:

  * **Container:** A lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries, and settings.
  * **Docker Compose:** A tool for defining and running multi-container Docker applications. It uses a YAML file to configure the application's services.
  * **Docker Engine:** The core technology that runs and manages Docker containers on your host machine.
  * **Environment Variables:** Dynamic named values that can affect the way running processes behave. Used in ImmutableInk to configure settings like database connections and application keys.
  * **Hash (Digital Fingerprint):** A unique, fixed-size string generated from data. Used for integrity verification in ImmutableInk.
  * **Persistent Storage:** Data storage that retains its content even after the process that created it has terminated or the container is removed. Essential for databases and application data.
  * **Port:** A communication endpoint in a computer networking connection. Used to identify specific applications or services on a network device.
  * **Reverse Proxy:** A server that sits in front of web servers and forwards client requests to those web servers. Provides benefits like load balancing, SSL termination, and security.
  * **SSL/TLS:** (Secure Sockets Layer/Transport Layer Security) Cryptographic protocols that provide secure communication over a computer network. Essential for HTTPS.
  * **YAML:** (YAML Ain't Markup Language) A human-friendly data serialization standard often used for configuration files, like `docker-compose.yml`.

<!-- end list -->

```
