apiVersion: apps/v1
kind: Deployment
metadata:
  name: multi-container-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: multi-app
  template:
    metadata:
      labels:
        app: multi-app
    spec:
      containers:

      # 🔹 MAIN CONTAINER (SIMPLE HTTP SERVER)
      - name: web-app
        image: registry.access.redhat.com/ubi8/python-39
        command:
        - python3
        - -m
        - http.server
        - "8080"
        volumeMounts:
        - name: shared-data
          mountPath: /app
        workingDir: /app
        ports:
        - containerPort: 8080

      # 🔹 SIDECAR CONTAINER
      - name: log-writer
        image: registry.access.redhat.com/ubi8/ubi-minimal
        command:
        - sh
        - -c
        - |
          while true; do
            echo "<h1>Updated at $(date)</h1>" > /data/index.html;
            sleep 5;
          done
        volumeMounts:
        - name: shared-data
          mountPath: /data

      volumes:
      - name: shared-data
        emptyDir: {}