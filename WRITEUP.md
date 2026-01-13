# Write-up

## Analyze, choose, and justify the appropriate resource option for deploying the app

For deploying the **Article CMS application** on Microsoft Azure, two primary deployment options were evaluated: **Azure Virtual Machine (VM)** and **Azure App Service**.  
The evaluation was based on **cost, scalability, availability, and development workflow**.

---

### Azure Virtual Machine (VM)

**Cost:**  
Azure Virtual Machines provide flexible pricing based on the selected VM size. For this project, a small VM instance was sufficient, keeping infrastructure costs relatively low. There are no additional platform-level charges beyond compute, storage, and networking, making it cost-effective for a small CMS application.

**Scalability:**  
Scalability on a VM is largely manual and requires resizing the VM or adding additional instances. While this approach is not ideal for high-traffic production systems, it is acceptable for a learning-focused or demonstration CMS where traffic is predictable and limited.

**Availability:**  
Availability depends on VM uptime and user-managed configurations. While Azure offers reliable infrastructure, tasks such as operating system updates, restarts, monitoring, and recovery must be handled manually. For this project, strict high availability was not a critical requirement.

**Workflow:**  
Using a VM provided full control over the environment. This made it easier to configure Python, Flask, HTTPS, Microsoft Authentication (MSAL), logging, SQL database connectivity, and Azure Blob Storage. Debugging was straightforward because application logs, configuration files, and system settings were directly accessible.

---

### Azure App Service

**Cost:**  
Azure App Service pricing depends on the selected service plan. Although it removes the need for infrastructure management, it can be more expensive than a small VM for a simple application with limited usage.

**Scalability:**  
App Service offers built-in automatic scaling and load balancing, making it well suited for applications with unpredictable or high traffic.

**Availability:**  
High availability is built into Azure App Service, as Microsoft manages the underlying infrastructure, operating system, and runtime environment.

**Workflow:**  
Despite its advantages, Azure App Service proved difficult to configure for this project. Multiple deployment issues were encountered, including application startup failures and “Application not available” errors. Troubleshooting was challenging due to limited control over the runtime environment and reduced visibility into system-level configurations.

---

### Final Choice

For this project, **Azure Virtual Machine (VM)** was selected as the deployment resource.

The VM approach enabled faster setup, easier debugging, and greater control over the application environment. This allowed successful configuration of HTTPS, Microsoft authentication, logging, database connections, and Azure Blob Storage within the project timeline. Given the project scope and learning objectives, the VM was the most appropriate and practical choice for deploying the CMS application.

---

## Assess app changes that would change My decision

If the application were expected to support a large number of users, require automatic scaling, or guarantee high availability, **Azure App Service** would become the preferred deployment option.

To support this transition, several changes would be necessary:
- Improved environment-based configuration using environment variables.
- Better application startup handling to meet App Service runtime requirements.
- Integration with managed services such as **Azure Key Vault** for secure secrets management.
- A more optimized deployment pipeline to reduce configuration issues during startup.

With these improvements, Azure App Service would provide better scalability, availability, and long-term operational efficiency for a production-grade CMS application.
