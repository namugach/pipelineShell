import sys
from pathlib import Path

# Base directory and path settings
base_dir = Path('/home/ubuntu/run')
sys.path.insert(0, str(base_dir))

# Import necessary modules
from config.config import server_infos
from util.util import send_ssh_comm

# Function to get the Docker image command
def get_remote_container_image_list(command):
	return f'docker image {command}'

# Main execution
if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Usage: python docker_image_list.py <command> [options]")
		sys.exit(1)

	command = " ".join(sys.argv[1:])

	for info in server_infos:
		ssh_command = get_remote_container_image_list(command)
		send_ssh_comm(info.name, f"{info.name}: 이미지 확인", ssh_command)
