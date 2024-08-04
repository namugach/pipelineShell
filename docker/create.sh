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

# 각 서버별 스크립트 경로
scripts=("container/server1.sh" "container/server2.sh" "container/server3.sh")

# 각 서버에서 Docker 컨테이너 실행
for i in "${!ips[@]}"; do
	start_service "Docker 컨테이너" "${scripts[$i]}"
done
