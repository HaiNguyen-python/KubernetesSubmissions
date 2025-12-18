## Exercise 3.9: DBaaS vs DIY Comparison

| Feature | DBaaS (Google Cloud SQL) | DIY (Database on K8s) |
| :--- | :--- | :--- |
| **Initial Work** | Easy. Provisioned via Cloud Console. | High. Must manage StatefulSets and PV/PVC. |
| **Maintenance** | Minimal. Provider handles OS/DB patches. | High. You handle all updates and security. |
| **Backup** | Automated & built-in. | Manual. Requires custom scripts/tools. |
| **Cost** | Higher (Service fee included). | Lower (Raw resource cost only). |
