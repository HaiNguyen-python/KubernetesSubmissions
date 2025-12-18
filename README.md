# Kubernetes Submissions

My solutions for the DevOps with Kubernetes course.
## Exercises
### Chapter 1
* [1.1.](./log_output)
* [1.2.](./the_project)
* [1.3.](./log_output)
* [1.4.](./the_project)
* [1.5.](./the_project)
* [1.6.](./the_project)
* [1.7.](./log_output)
* [1.8.](./the_project)
* [1.9.](./ping_pong)
* [1.10.](./log_output)
* [1.11.](./log_output)
* [1.12.](./the_project)
* [1.13.](./the_project)
### Chapter 2
* [2.1.](./log_output)
* [2.2.](./the_project)
* [2.3.](./log_output)
* [2.4.](./the_project)
* [2.5.](./log_output)
* [2.6.](./the_project)
* [2.7.](./ping_pong)
* [2.8.](./the_project)
* [2.9.](./the_project)
* [2.10.](./the_project)
## Chapter 3
* [3.1.](./ping_pong)
* [3.2.](./log_output)
* [3.3.](./ping_pong)
* [3.4.](./ping_pong)
* [3.5.](./the_project)
* [3.6.](./the_project)
* [3.7.](./the_project)

* [3.8.](./the_project)

* [3.9.](./the_project)

## Exercise 3.9: DBaaS vs DIY Comparison

| Feature | DBaaS (e.g., Google Cloud SQL) | DIY (Database on K8s) |
| :--- | :--- | :--- |
| **Initial Work** | Easy. A few clicks/commands to provision. | High. Need to configure StorageClasses, StatefulSets, and Services. |
| **Initial Cost** | Higher (pay for the managed service & overhead). | Lower (pay only for raw compute & disk). |
| **Maintenance** | Minimal. Cloud provider handles OS & DB patches. | High. You are responsible for all updates and security. |
| **Backup/Restore** | Automated & Built-in. Easy point-in-time recovery. | Manual. Need to configure CronJobs/Tools (like Velero) for snapshots. |
| **Ease of Use** | Very high. Specialized tools and dashboard provided. | Medium. Requires deep knowledge of K8s and DB administration. |

**Conclusion:** DBaaS is preferred for production environments where reliability and low maintenance are critical. DIY is suitable for cost-saving in development or when strict custom configurations are required.

* [3.9.](./the_project)

## Exercise 3.9: DBaaS vs DIY Comparison

| Feature | DBaaS (Google Cloud SQL) | DIY (Database on K8s) |
| :--- | :--- | :--- |
| **Initial Work** | Low. Managed service is easy to provision. | High. Requires complex StatefulSet/Storage config. |
| **Costs** | Higher monthly fee for managed overhead. | Lower raw infrastructure cost. |
| **Maintenance** | Minimal. Cloud provider handles patches/OS. | High. User handles all updates and security. |
| **Backup** | Built-in, automated, and reliable. | Manual. Requires custom scripts/tools (Velero). |

* [3.9.](./the_project)

## Exercise 3.9: DBaaS vs DIY Comparison

| Feature | DBaaS (e.g., Google Cloud SQL) | DIY (Database on K8s) |
| :--- | :--- | :--- |
| **Initial Work** | Easy. Provisioned via API/Console in minutes. | High. Requires StatefulSet, PV/PVC, and Service config. |
| **Initial Cost** | Higher due to managed service overhead. | Lower raw infrastructure cost. |
| **Maintenance** | Minimal. Provider handles OS/DB patching. | High. You manage updates, security, and scaling. |
| **Backup/Restore** | Automated, point-in-time recovery built-in. | Manual. Requires tools like Velero or custom scripts. |
| **Ease of Use** | Very high. Specialized dashboards provided. | Medium. Requires K8s and DB admin expertise. |

## Exercise 3.9: DBaaS vs DIY Comparison

| Feature | DBaaS (e.g., Google Cloud SQL) | DIY (Database on K8s) |
| :--- | :--- | :--- |
| **Initial Work** | Easy. Fast provisioning via Cloud Console. | High. Must manage StatefulSets and Storage. |
| **Maintenance** | Minimal. Provider handles updates/patches. | High. You handle OS/DB security and updates. |
| **Backup** | Automated & built-in. | Manual. Requires custom tools (e.g. Velero). |
| **Cost** | Higher (Service fee included). | Lower (Raw resource cost only). |

* [3.9.](./the_project)

* [3.9.](./the_project)
