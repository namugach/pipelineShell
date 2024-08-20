import sys
from pathlib import Path
import asyncio
import asyncssh

# Base directory and path settings
base_dir = Path('/root/run')
sys.path.insert(0, str(base_dir))

# Import necessary modules
from config.config import server_infos

# Function to get the Docker image command
def get_pull(command):
	return f'docker pull {command}'

# 비동기 SSH 명령 전송 함수
async def send_ssh_comm_async(name, description, command):
	print(f"Executing on {name}: {command}")
	
	try:
		async with asyncssh.connect(name, known_hosts=None) as conn:
			async with conn.create_process(command) as process:
				# 실시간으로 stdout과 stderr를 읽어 출력
				async for line in process.stdout:
					print(f"[{name} STDOUT] {line.strip()}")
				async for line in process.stderr:
					print(f"[{name} STDERR] {line.strip()}")

		print(f"Completed on {name}: {description}")

	except asyncssh.Error as exc:
		print(f'SSH connection failed: {exc}')

# 비동기 실행 함수
async def execute_pull_command(info, command):
	ssh_command = get_pull(command)
	await send_ssh_comm_async(info.name, f"{info.name}: 당겨오는 중...", ssh_command)

# Main execution
if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Usage: python pull.py <command> [options]")
		sys.exit(1)

	command = " ".join(sys.argv[1:])

	# 비동기 메인 함수
	async def main():
		tasks = [execute_pull_command(info, command) for info in server_infos]
		await asyncio.gather(*tasks)

	# 비동기 함수 실행
	asyncio.run(main())
