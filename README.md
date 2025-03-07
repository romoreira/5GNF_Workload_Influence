# Project: Metrics Integration and Stress Testing

This project aims to integrate and analyze performance metrics in a Kubernetes environment, using scripts to collect data and tools like ChaosMesh to inject workload and observe system behavior.

## Prerequisites

- Python 3.8+
- Configured Kubernetes cluster
- Installed ChaosMesh with GUI
- Basic command-line tools (kubectl, etc.)

## Steps to Run the Experiment

```bash
#!/bin/bash

# Step 1: Set up environment
echo "Setting up environment..."

# Step 2: Run experiment-runner.sh
echo "Running experiment-runner.sh..."
./experiment-runner.sh

# Step 3: Deploy a test pod and run sensor_script.py
echo "Deploying test pod and running sensor_script.py..."
kubectl apply -f test-pod.yaml
python3 sensor_script.py

# Step 4: Install ChaosMesh with GUI
echo "Installing ChaosMesh with GUI..."
# (Include your specific ChaosMesh installation commands here)
# Example:
# kubectl create -f https://mirrors.chaos-mesh.org/v2.0.3/chaos-mesh.yaml
# kubectl port-forward -n chaos-testing svc/chaos-dashboard 2333:2333

# Step 5: Configure the Keys and Auth for ChaosMesh operation in your Kubernetes Cluster
echo "Configuring keys and authentication for ChaosMesh..."
# (Include your specific key and authentication setup commands here)

# Step 6: Apply RBAC to enable ChaosMesh to inject workload into the Cluster
echo "Applying RBAC for ChaosMesh..."
kubectl apply -f rbac.yaml

# Step 7: Get the token to input into ChaosMesh GUI
echo "Getting the token for ChaosMesh GUI..."
TOKEN=$(kubectl create token account-cluster-manager-qwbio)
echo "Token: $TOKEN"

# Step 8: Join CSV files with metrics and stress events
echo "Joining CSV files..."
python3 join_metrics.py

echo "All steps completed successfully!"

