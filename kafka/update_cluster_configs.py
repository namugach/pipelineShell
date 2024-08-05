import sys
from pathlib import Path
from typing import List
base_dir = Path('/home/ubuntu/run')
sys.path.insert(0, str(base_dir))
from config.config import update_infos
from config.config import ServerInfo
from util.util import send_ssh_comm




MYID_PATH = "/home/ubuntu/zkdata/myid"
SERVER_PROPERTIES_PATH = "~/app/kafka/kafka_2.13-3.6.2/config/server.properties"
ZOOKEEPER_PROPERTIES_PATH = "~/app/kafka/kafka_2.13-3.6.2/config/zookeeper.properties"
START_SERVER_PATH = "~/run/kafka/start_server.sh"
START_ZOOKEEPR_PATH = "~/run/kafka/start_zookeeper.sh"

def update_server(server_info:ServerInfo, update_infos:List [ServerInfo]=update_infos):
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
		f"sed -i 's/^zookeeper.connect=.*/zookeeper.connect={update_infos[0].ip}:2181,{update_infos[1].ip}:2181,{update_infos[2].ip}:2181/' {SERVER_PROPERTIES_PATH}",
		
		# zookeeper.properties 파일 업데이트
		f"sed -i 's|^server.1=.*|server.1={update_infos[0].ip}:2888:3888|' {ZOOKEEPER_PROPERTIES_PATH}",
		f"sed -i 's|^server.2=.*|server.2={update_infos[1].ip}:2888:3888|' {ZOOKEEPER_PROPERTIES_PATH}",
		f"sed -i 's|^server.3=.*|server.3={update_infos[2].ip}:2888:3888|' {ZOOKEEPER_PROPERTIES_PATH}"
		


	]
	for cmd in commands:
		send_ssh_comm(name, f"{name} - 명령어 실행", cmd, port)

	print(f"Updated {name}")

for info in update_infos:
	update_server(info, update_infos)

print("All servers updated successfully.")
