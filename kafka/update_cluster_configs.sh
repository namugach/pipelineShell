#!/bin/bash

# 서버 목록과 각 서버에 해당하는 ID와 IP 주소 설정
declare -A servers
servers=(
	["server1"]="1 172.17.0.2"
	["server2"]="2 172.17.0.3"
	["server3"]="3 172.17.0.4"
)

# 파일 경로 설정
MYID_PATH="/home/ubuntu/zkdata/myid"
SERVER_PROPERTIES_PATH="~/app/kafka/kafka_2.13-3.6.2/config/server.properties"

for server in "${!servers[@]}"; do
	id_ip=(${servers[$server]})
	id=${id_ip[0]}
	ip=${id_ip[1]}

	echo "Updating $server with ID $id and IP $ip"

	# myid 파일 업데이트
	ssh "$server" "echo $id > $MYID_PATH"

	# server.properties 파일 업데이트
	ssh "$server" "sed -i 's/^broker.id=.*/broker.id=$id/' $SERVER_PROPERTIES_PATH"
	ssh "$server" "sed -i 's|^listeners=PLAINTEXT://.*|listeners=PLAINTEXT://$ip:9092|' $SERVER_PROPERTIES_PATH"
	ssh "$server" "sed -i 's|^advertised.listeners=PLAINTEXT://.*|advertised.listeners=PLAINTEXT://$ip:9092|' $SERVER_PROPERTIES_PATH"

	echo "Updated $server"
done

echo "All servers updated successfully."