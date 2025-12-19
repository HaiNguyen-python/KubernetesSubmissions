# Kubernetes Submissions

## GKE Deployment Status
* **External IP:** http://35.228.137.215
* **GitHub Actions:** Fixed workflow path in main.yml (line 28). Status is Green.
* **Technical Note:** The application is deployed. However, due to the Postgres service being restricted to the `project` namespace, the ping-pong app in the `default` namespace currently has a connection delay.

## Verified with:
`curl -H "Host: ping-pong-serverless.default.sslip.io" http://35.228.137.215`
