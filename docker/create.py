import sys, subprocess, time
from pathlib import Path

base_dir = Path('/home/ubuntu/run')
sys.path.insert(0, str(base_dir))
from config.config import server_infos

def create_container(
	name, port=2222, server_infos=server_infos, ssh_key=""
):
	return f'''
	docker container run -itd \\
		--name {name} \\
		--hostname {name} \\
		--add-host {server_infos[0].name}:{server_infos[0].ip} \\
		--add-host {server_infos[1].name}:{server_infos[1].ip} \\
		--add-host {server_infos[2].name}:{server_infos[2].ip} \\
		-p {port}:{port} \\
		namugach/ubuntu-pipeline:24.04-kafka-test \\
		/bin/bash -c f"{ssh_key} >> /home/ubuntu/.ssh/authorized_keys"
	'''


for info in server_infos:
	ssh_command = [
		'ssh',
		'-o', 'StrictHostKeyChecking=no',
		info.name,
		create_container(info.name)
	]
	print(f"=========={info.name} 생성 중...========")
	subprocess.run(ssh_command, capture_output=True, text=True)
	time.sleep(1)
