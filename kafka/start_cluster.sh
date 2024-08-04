#!/bin/bash

ips=("server1" "server2" "server3")

start_service() {
	local service_name=$1
	local script_path=$2
	local sleep_time=${3:-1} # 기본값을 1로 설정

	for ip in "${ips[@]}"; do
		echo ""
		echo "============== $service_name 시작 시도 중: $ip =============="
		echo ""
		ssh -o StrictHostKeyChecking=no -o ConnectTimeout=5 $ip 'bash -s' < "$script_path"
		sleep $sleep_time
		if [ $? -eq 0 ]; then
			echo "$ip 에서 $service_name 가 성공적으로 시작되었어"
		else
			echo "$ip 에서 $service_name 시작 실패"
			exit 1
		fi
	done
}

# Zookeeper 시작 및 상태 확인
start_service "Zookeeper" "./run/kafka/start_zookeeper.sh"

# 대기
sleep 3

# Kafka 서버 시작
start_service "Kafka 서버" "./run/kafka/start_server.sh" 2

# Kafka check
start_service "Kafka check" "./run/kafka/check_conn.sh" 2