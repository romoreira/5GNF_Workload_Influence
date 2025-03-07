# 🚀 Experiment Runner

## ▶️ Run `experiment-runner.sh`
Start the experiment by running the script:

```bash
./experiment-runner.sh
```

## 🏗️ Deploy a Test Pod and Run `sensor_script.py`
Create a test pod in Kubernetes and execute the sensor script:

```bash
kubectl apply -f test-pod.yaml
python3 sensor_script.py
```

## 🔥 Install Chaos Mesh with GUI
Install Chaos Mesh with GUI support:

```bash
kubectl apply -f https://mirrors.chaos-mesh.org/latest.yaml
```

Once installed, access the GUI to manage stress tests.

## 🔑 Configure Keys and Authentication for Chaos Mesh in Your Kubernetes Cluster
Ensure that authentication and necessary keys are set up for Chaos Mesh to operate within your Kubernetes cluster.

## 🔧 Apply RBAC to Enable Chaos Mesh to Inject Workload into the Cluster
To allow Chaos Mesh to inject workloads, apply the necessary Role-Based Access Control (RBAC) settings:

```bash
kubectl apply -f rbac.yaml
```

## 🔐 Get the Token for Chaos Mesh GUI Access
Retrieve the token needed for logging into the Chaos Mesh GUI:

```bash
kubectl create token account-cluster-manager-qwbio
```

Use this token to access and manage experiments in the Chaos Mesh GUI.

🎯 **Now you're ready to run experiments and monitor your Kubernetes workloads!** 🚀

