#!/bin/bash

# ssh_action.sh 파일을 불러옴
source /home/ubuntu/run/util/ssh_action.sh

# 각 서버별 스크립트 경로
scripts=(
	"/home/ubuntu/run/docker/container/server1.sh"
	"/home/ubuntu/run/docker/container/server2.sh"
	"/home/ubuntu/run/docker/container/server3.sh"
)

# 각 서버에서 Docker 컨테이너 실행
for i in "${!ips[@]}"; do
	start_service "Docker 컨테이너" "${scripts[$i]}"
done
