#!/bin/bash

ips=(
  "server1"
  "server1 -p 2222"
  "server2"
  "server2 -p 2222"
  "server3"
  "server3 -p 2222"
)

# SSH 키 파일 (필요하면 경로 지정)
# key_file="~/.ssh/id_rsa"

# 각 IP에 대해 SSH 접속 시도
for ip in "${ips[@]}"; do
    echo "접속 시도 중: $ip"
    ssh -o ConnectTimeout=5 $ip "echo '접속 성공: $ip'"
    if [ $? -eq 0 ]; then
        echo "$ip 에 성공적으로 접속했어"
    else
        echo "$ip 에 접속 실패"
    fi
done
