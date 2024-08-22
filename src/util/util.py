import subprocess, asyncio, asyncssh
# pip install asyncssh

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
	
# 비동기 SSH 명령 전송 함수
async def send_ssh_comm_async(name, description, command):
	print(f"Executing on {name}: {command}")
	
	try:
		async with asyncssh.connect(name, known_hosts=None) as conn:
			async with conn.create_process(command) as process:
				stdout, stderr = await process.communicate()
				
				print(f"[{name} STDOUT] {stdout}")
				if stderr:
					print(f"[{name} STDERR] {stderr}")

		print(f"Completed on {name}: {description}")

	except asyncssh.Error as exc:
		print(f'SSH connection failed: {exc}')
