import sys, time
from pathlib import Path

base_dir = Path('/root/run')
sys.path.insert(0, str(base_dir))
from config.config import server_infos
from util.util import send_ssh_comm


here_dir = f"{base_dir}/kafka"
start_zookeeper_path_file = f"{here_dir}/start_zookeeper.sh"
start_server_path_file = f"{here_dir}/start_server.sh"
check_conn_path_file = f"{here_dir}/check_conn.sh"


with open(start_zookeeper_path_file, 'r') as file:
	start_zookeeper__sh = file.read()
	
with open(start_server_path_file, 'r') as file:
	start_server__sh = file.read()
	
with open(check_conn_path_file, 'r') as file:
	check_conn__sh = file.read()



print("====================주키퍼 서버 켜는 중...====================")
for info in server_infos:
	send_ssh_comm(info.name, f"{info.name}: start_zookeeper", start_zookeeper__sh, info.port)
	time.sleep(1)
	send_ssh_comm(info.name, f"{info.name}: check_conn", check_conn__sh, info.port)
print("")
print("")


print("====================주키퍼가 들어오는 중...====================")
time.sleep(1)
print("엉")
time.sleep(1)
print("거")
time.sleep(1)
print("주")
time.sleep(1)
print("춤")

print("====================카프카 서버 켜는 중...====================")
for info in server_infos:
	send_ssh_comm(info.name, f"{info.name}: start_server", start_server__sh, info.port)
	time.sleep(1)
	send_ssh_comm(info.name, f"{info.name}: check_conn", check_conn__sh, info.port)
print("")
print("")

print("====================모두 확인 중...====================")
for info in server_infos:
	time.sleep(1)
	send_ssh_comm(info.name, f"{info.name}: check_conn", check_conn__sh, info.port)