
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
