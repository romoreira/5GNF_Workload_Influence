#!/bin/bash

echo "Creating CSV file"
output_file="stress_events.csv"
echo "nf,stress_test,begin_timestamp,end_timestamp" > $output_file

echo "Iterating over pods"
while true; do

  pods=$(kubectl get pods --no-headers -o custom-columns=":metadata.name" | grep -E "^free5gc|^ueransim-gnb")

  for pod in $pods; do
    nf_name=$(echo "$pod" | awk -F'-' '{print $1"-"$2}')
    echo "Benchmarking: $nf_name"

    # =================== CPU TEST ===================
    echo "Starting CPU stress test"

    cpu_load=50
    duration=20

    cat <<EOF > "cpu-${cpu_load}-${pod}-stress.yaml"
kind: StressChaos
apiVersion: chaos-mesh.org/v1alpha1
metadata:
  namespace: default
  name: cpu-stress-${nf_name}
spec:
  selector:
    namespaces:
      - default
    pods:
      default:
        - ${pod}
  mode: one
  stressors:
    cpu:
      workers: 10
      load: ${cpu_load}
  duration: '${duration}s'
EOF

    start_time=$(date +%s)
    kubectl apply -f "cpu-${cpu_load}-${pod}-stress.yaml"
    sleep $duration
    end_time=$(date +%s)

    echo "$nf_name,CPU_${cpu_load}_Duration_${duration},$start_time,$end_time" >> $output_file
    rm "cpu-${cpu_load}-${pod}-stress.yaml"
    kubectl delete stresschaos cpu-stress-${nf_name}

    echo "CPU stress test completed for $nf_name"

    # =================== MEMORY TEST ===================
    echo "Starting Memory stress test"

    memory_load=512
    duration=20

    cat <<EOF > "mem-${memory_load}-${pod}-stress.yaml"
kind: StressChaos
apiVersion: chaos-mesh.org/v1alpha1
metadata:
  namespace: default
  name: mem-stress-${nf_name}
spec:
  selector:
    namespaces:
      - default
    pods:
      default:
        - ${pod}
  mode: one
  stressors:
    memory:
      workers: 4
      size: '${memory_load}MiB'
  duration: '${duration}s'
EOF

    start_time=$(date +%s)
    kubectl apply -f "mem-${memory_load}-${pod}-stress.yaml"
    sleep $duration
    end_time=$(date +%s)

    echo "$nf_name,MEMORY_${memory_load}_Duration_${duration},$start_time,$end_time" >> $output_file
    rm "mem-${memory_load}-${pod}-stress.yaml"
    kubectl delete stresschaos mem-stress-${nf_name}

    echo "Memory stress test completed for $nf_name"

    # =================== CPU + MEMORY TEST ===================
    echo "Starting CPU + Memory stress test simultaneously"

    cpu_load=50
    memory_load=512
    duration=20

    cat <<EOF > "cpu-mem-${cpu_load}-${memory_load}-${pod}-stress.yaml"
kind: StressChaos
apiVersion: chaos-mesh.org/v1alpha1
metadata:
  namespace: default
  name: cpu-mem-stress-${nf_name}
spec:
  selector:
    namespaces:
      - default
    pods:
      default:
        - ${pod}
  mode: one
  stressors:
    cpu:
      workers: 10
      load: ${cpu_load}
    memory:
      workers: 4
      size: '${memory_load}MiB'
  duration: '${duration}s'
EOF

    start_time=$(date +%s)
    kubectl apply -f "cpu-mem-${cpu_load}-${memory_load}-${pod}-stress.yaml"
    sleep $duration
    end_time=$(date +%s)

    echo "$nf_name,CPU_${cpu_load}_MEMORY_${memory_load}_Duration_${duration},$start_time,$end_time" >> $output_file
    rm "cpu-mem-${cpu_load}-${memory_load}-${pod}-stress.yaml"
    kubectl delete stresschaos cpu-mem-stress-${nf_name}

    echo "CPU + Memory stress test completed for $nf_name"

    # =================== WAIT TIME BETWEEN TESTS ===================
    sleep_time=$((1 + RANDOM % 10))
    echo "Waiting $sleep_time seconds before testing the next NF..."
    sleep $sleep_time

  done
  exit
done

