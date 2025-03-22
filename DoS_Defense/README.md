# 5GNF DoS Defense

This repository contains a machine learning project focused on training models to detect and defend against Denial of Service (DoS) attacks in Kubernetes deployments. The models are trained using monitoring parameters to identify potential threats and take appropriate defensive actions.

## Features

- **DoS Attack Detection**: Utilizes machine learning algorithms to detect DoS attacks based on monitoring data.
- **Kubernetes Integration**: Seamlessly integrates with Kubernetes deployments to provide real-time defense mechanisms.
- **Monitoring Parameters**: Analyzes various monitoring parameters to identify abnormal patterns indicative of DoS attacks.
- **Automated Defense**: Implements automated responses to mitigate detected threats and ensure the stability of the deployment.

## Getting Started

### Prerequisites

- Kubernetes cluster
- Python 3.6+
- Required Python libraries (listed in `requirements.txt`)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/5GNF_DoS_Defense.git
    cd 5GNF_DoS_Defense
    ```

2. Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. Train the machine learning model:
    ```bash
    python train_model.py
    ```

2. Deploy the defense mechanism in your Kubernetes cluster:
    ```bash
    kubectl apply -f deployment.yaml
    ```

3. Monitor the logs to see the defense mechanism in action:
    ```bash
    kubectl logs -f <pod-name>
    ```

## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) for more information.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Special thanks to the open-source community for providing valuable resources and tools.
