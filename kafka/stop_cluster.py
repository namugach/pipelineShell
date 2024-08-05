
import sys, time
from pathlib import Path

base_dir = Path('/home/ubuntu/run')
sys.path.insert(0, str(base_dir))
from config.config import server_infos
from util.util import send_ssh_comm

here_dir = f"{base_dir}/kafka"
stop_server_path_file = f"{here_dir}/stop_server.sh"
check_conn_path_file = f"{here_dir}/check_conn.sh"

with open(stop_server_path_file, 'r') as file:
	stop_server__sh = file.read()
with open(check_conn_path_file, 'r') as file:
	check_conn__sh = file.read()

print("====================종료 중...====================")
for info in server_infos:
	send_ssh_comm(info.name, f"{info.name}: stop_server", stop_server__sh, info.port)
	time.sleep(1)
	send_ssh_comm(info.name, f"{info.name}: check_conn", check_conn__sh, info.port)