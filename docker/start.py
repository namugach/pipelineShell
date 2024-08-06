import sys
from pathlib import Path

base_dir = Path('/home/ubuntu/run')
sys.path.insert(0, str(base_dir))
from config.config import server_infos
from util.util import send_ssh_comm

def get_remote_container_start(name):

	return f'''
	docker container start {name}
	'''


for info in server_infos:
	send_ssh_comm(info.name, f"{info.name}: 제거", get_remote_container_start(info.name))