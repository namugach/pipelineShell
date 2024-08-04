import subprocess

def send_ssh_comm(host, name, comm):
	ssh_command = [
		'ssh',
		'-o', 'StrictHostKeyChecking=no',
		host, comm
	]
	print(f"=========={name} 실행...========")
	run = subprocess.run(ssh_command, capture_output=True, text=True)
	print(run.stdout)
