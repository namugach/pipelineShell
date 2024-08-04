#!/bin/bash

ips=("server1" "server2" "server3")

# Zookeeper 시작 및 상태 확인
for ip in "${ips[@]}"; do
	echo "Kafka 서버 중지 시도 중: $ip"
	ssh -o StrictHostKeyChecking=no -o ConnectTimeout=5 $ip 'bash -s' < ./run/kafka/stop_server.sh
	sleep 1
	if [ $? -eq 0 ]; then
			echo "$ip 에서 Kafka 서버가 성공적으로 중지 됐어"
	else
			echo "$ip 에서 Kafka 서버 중지 실패"
			exit 1
	fi
done
