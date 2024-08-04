#!/bin/bash

# 서버 목록과 각 서버에 해당하는 ID와 IP 주소 설정
declare -A servers
servers=(
	["server1"]="1 172.31.14.186"
	["server2"]="3 172.31.10.99"
	["server3"]="2 172.31.1.229"
)

get_ip_address() {
	local server_name=$1
	local value=${servers[$server_name]}
	local ip_address=$(echo $value | awk '{print $2}')
	echo $ip_address
}


# 파일 경로 설정
MYID_PATH="/home/ubuntu/zkdata/myid"
SERVER_PROPERTIES_PATH="~/app/kafka/kafka_2.13-3.6.2/config/server.properties"
ZOOKEEPER_PROERTIES_PATH="~/app/kafka/kafka_2.13-3.6.2/config/zookeeper.properties"

# ZOOKEEPER_CONNECT ip정보
ZOOKEEPER_CONNECT=$(get_ip_address "server1"):2181,$(get_ip_address "server2"):2181,$(get_ip_address "server3"):2181

for server in "${!servers[@]}"; do
	id_ip=(${servers[$server]})
	id=${id_ip[0]}
	ip=${id_ip[1]}

	echo "Updating $server with ID $id and IP $ip"
	# myid 파일 업데이트
	ssh -p 2222 "$server" "echo $id > $MYID_PATH"
	# server.properties 파일 업데이트
	ssh -p 2222 "$server" "sed -i 's/^broker.id=.*/broker.id=$id/' $SERVER_PROPERTIES_PATH"
	ssh -p 2222 "$server" "sed -i 's|^listeners=PLAINTEXT://.*|listeners=PLAINTEXT://$ip:9092|' $SERVER_PROPERTIES_PATH"
	ssh -p 2222 "$server" "sed -i 's|^advertised.listeners=PLAINTEXT://.*|advertised.listeners=PLAINTEXT://$ip:9092|' $SERVER_PROPERTIES_PATH"
	ssh -p 2222 "$server" "sed -i 's/^zookeeper.connect=.*/zookeeper.connect=$ZOOKEEPER_CONNECT/' $SERVER_PROPERTIES_PATH"

	# zookeeper.properties 파일 업데이트
	ssh -p 2222 "$server" "sed -i 's|^server.1=.*|server.1=$(get_ip_address "server1"):2888:3888|' $ZOOKEEPER_PROERTIES_PATH"
	ssh -p 2222 "$server" "sed -i 's|^server.2=.*|server.2=$(get_ip_address "server2"):2888:3888|' $ZOOKEEPER_PROERTIES_PATH"
	ssh -p 2222 "$server" "sed -i 's|^server.3=.*|server.3=$(get_ip_address "server3"):2888:3888|' $ZOOKEEPER_PROERTIES_PATH"

	echo "Updated $server"
done

echo "All servers updated successfully."
