import sys, time
from pathlib import Path
from typing import List
base_dir = Path('/home/ubuntu/run')
sys.path.insert(0, str(base_dir))
from config.config import server_infos
from config.config import ServerInfo
from util.util import send_ssh_comm




MYID_PATH = "/home/ubuntu/zkdata/myid"
SERVER_PROPERTIES_PATH = "~/app/kafka/kafka_2.13-3.6.2/config/server.properties"
ZOOKEEPER_PROPERTIES_PATH = "~/app/kafka/kafka_2.13-3.6.2/config/zookeeper.properties"


def update_server(server_info:ServerInfo, server_infos:List [ServerInfo]=server_infos):
	# myid 파일 업데이트
	id = server_info.id 
	ip = server_info.ip
	name = server_info.name
	port = server_info.port
	
	send_ssh_comm(name, f"{name} - myid 업데이트", f"echo {id} > {MYID_PATH}", port)
	
	commands = [
		# server.properties 파일 업데이트
		f"sed -i 's/^broker.id=.*/broker.id={id}/' {SERVER_PROPERTIES_PATH}",
		f"sed -i 's|^listeners=PLAINTEXT://.*|listeners=PLAINTEXT://{ip}:9092|' {SERVER_PROPERTIES_PATH}",
		f"sed -i 's|^advertised.listeners=PLAINTEXT://.*|advertised.listeners=PLAINTEXT://{ip}:9092|' {SERVER_PROPERTIES_PATH}",
		f"sed -i 's/^zookeeper.connect=.*/zookeeper.connect={server_infos[0].ip}:2181,{server_infos[1].ip}:2181,{server_infos[2].ip}:2181/' {SERVER_PROPERTIES_PATH}",
		
		# zookeeper.properties 파일 업데이트
		f"sed -i 's|^server.1=.*|server.1={server_infos[0].ip}:2888:3888|' {ZOOKEEPER_PROPERTIES_PATH}",
		f"sed -i 's|^server.2=.*|server.2={server_infos[1].ip}:2888:3888|' {ZOOKEEPER_PROPERTIES_PATH}",
		f"sed -i 's|^server.3=.*|server.3={server_infos[2].ip}:2888:3888|' {ZOOKEEPER_PROPERTIES_PATH}"
	]

	for cmd in commands:
		send_ssh_comm(name, f"{name} - 명령어 실행", cmd, port)

	print(f"Updated {name}")

# update_server(server_infos[0], server_infos)

for info in server_infos:
	# print(info)
	update_server(info, server_infos)

# for server, (id, ip) in servers.items():
# 	print(f"Updating {server} with ID {id} and IP {ip}")
# 	update_server(server, id, ip, zookeeper_connect)

print("All servers updated successfully.")
