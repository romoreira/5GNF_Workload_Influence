#

## Run experiment-runner.sh
## Deploy a test-pod and run sensor_script.py
## Intall ChaosMesh with GUI
## Configure the Keys and Auth for ChaosMesh operatin into you Kubernetes Cluster

## Aply the RBAC to enable ChaosMesh inject workload into Cluster
kubectl apply -f rbac.yaml


## To get the token to input it into Chaos Mesh GUI:
kubectl create token account-cluster-manager-qwbio
