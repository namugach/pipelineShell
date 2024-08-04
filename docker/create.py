import sys, time
from pathlib import Path

base_dir = Path('/home/ubuntu/run')
sys.path.insert(0, str(base_dir))
from config.config import server_infos
from util.util import send_ssh_comm

ssh_key_dir = "./config/keygen"
id_rsa_path = Path(ssh_key_dir) / "id_rsa"
id_rsa_pub_path = Path(ssh_key_dir) / "id_rsa.pub"

def get_create_container_comm(name, port=2222, server_infos=server_infos):
	with open(id_rsa_path, 'r') as id_rsa_file:
		id_rsa = id_rsa_file.read()
	
	with open(id_rsa_pub_path, 'r') as id_rsa_pub_file:
		id_rsa_pub = id_rsa_pub_file.read()
	
	return f'''
	docker container run -itd \\
		--name {name} \\
		--hostname {name} \\
		--add-host {server_infos[0].name}:{server_infos[0].ip} \\
		--add-host {server_infos[1].name}:{server_infos[1].ip} \\
		--add-host {server_infos[2].name}:{server_infos[2].ip} \\
		-p {port}:{port} \\
		namugach/ubuntu-pipeline:24.04-kafka-test \\
		/bin/bash -c "echo '{id_rsa}' > /home/ubuntu/.ssh/id_rsa && \\
				echo '{id_rsa_pub}' > /home/ubuntu/.ssh/id_rsa.pub && \\
				echo '{id_rsa_pub}' > /home/ubuntu/.ssh/authorized_keys && \\
				chmod 600 /home/ubuntu/.ssh/id_rsa && \\
				chmod 644 /home/ubuntu/.ssh/id_rsa.pub && \\
				sudo service ssh start && \\
				sudo service mysql start && \\
				tail -f /dev/null"
	'''

for info in server_infos:
	send_ssh_comm(info.name, info.name, get_create_container_comm(info.name))
	time.sleep(1)