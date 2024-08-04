import subprocess

def send_ssh_comm(host, name, comm, port=22):
	ssh_command = [
		'ssh',
		'-o', 'StrictHostKeyChecking=no',
		'-p', str(port),
		host, comm
	]
	print(f"=========={name} 실행...========")
	run = subprocess.run(ssh_command, capture_output=True, text=True)
	print(run.stdout)