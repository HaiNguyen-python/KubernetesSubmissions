import kopf
import kubernetes
import requests
import yaml

@kopf.on.create('stable.dwk', 'v1', 'dummysites')
def create_fn(spec, name, namespace, logger, **kwargs):
    url = spec.get('website_url')
    if not url:
        return {'error': 'website_url is required'}

    # Tải nội dung HTML
    response = requests.get(url)
    html = response.text

    api = kubernetes.client.CoreV1Api()
    apps_api = kubernetes.client.AppsV1Api()

    # 1. Tạo ConfigMap chứa index.html
    cm = kubernetes.client.V1ConfigMap(
        metadata=kubernetes.client.V1ObjectMeta(name=f"{name}-html"),
        data={"index.html": html}
    )
    api.create_namespaced_config_map(namespace, cm)

    # 2. Tạo Deployment chạy Nginx mount ConfigMap
    dep_yaml = f"""
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {name}-dep
spec:
  replicas: 1
  selector:
    matchLabels:
      app: {name}
  template:
    metadata:
      labels:
        app: {name}
    spec:
      containers:
      - name: nginx
        image: nginx:alpine
        volumeMounts:
        - name: html-volume
          mountPath: /usr/share/nginx/html
      volumes:
      - name: html-volume
        configMap:
          name: {name}-html
"""
    apps_api.create_namespaced_deployment(namespace, yaml.safe_load(dep_yaml))
    logger.info(f"DummySite {name} created for {url}")
