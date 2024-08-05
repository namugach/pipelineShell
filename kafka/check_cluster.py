import sys, time
from pathlib import Path

base_dir = Path('/home/ubuntu/run')
sys.path.insert(0, str(base_dir))
from config.config import server_infos
from util.util import send_ssh_comm


here_dir = f"{base_dir}/kafka"
check_conn_path_file = f"{here_dir}/check_conn.sh"



with open(check_conn_path_file, 'r') as file:
	check_conn__sh = file.read()


print("====================모두 확인 중...====================")
for info in server_infos:
	time.sleep(1)
	send_ssh_comm(info.name, f"{info.name}: check_conn", check_conn__sh, info.port)
print("")
print("")