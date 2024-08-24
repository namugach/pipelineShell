import asyncio
import subprocess

# ANSI escape codes for colors
COLORS = {
	"server1": "\033[91m",  # Red
	"server2": "\033[92m",  # Green
	"server3": "\033[94m",  # Blue
	"reset": "\033[0m"      # Reset to default
}

async def run_command(server, command):
	proc = await asyncio.create_subprocess_shell(
		f"ssh {server} '{command}'",
		stdout=subprocess.PIPE,
		stderr=subprocess.PIPE
	)

	async def read_output():
		while True:
			line = await proc.stdout.readline()
			if line:
				color = COLORS.get(server, COLORS["reset"])
				print(f"{color}[{server}]\n {line.decode().strip()}{COLORS['reset']}\n\n")
			else:
				break

	async def read_error():
		while True:
			line = await proc.stderr.readline()
			if line:
				color = COLORS.get(server, COLORS["reset"])
				print(f"{color}[{server} ERROR]\n {line.decode().strip()}{COLORS['reset']}\n\n")
			else:
				break

	await asyncio.gather(read_output(), read_error())
	await proc.wait()
	print(f"{COLORS.get(server, COLORS['reset'])}[{server}] done!{COLORS['reset']}\n\n")

async def main():
	commands = {
		"server1": "~/app/kafka/kafka_2.13-3.6.2/bin/kafka-console-consumer.sh --bootstrap-server 172.20.0.10:9092 --topic my_data",
		"server2": "~/app/kafka/kafka_2.13-3.6.2/bin/kafka-console-consumer.sh --bootstrap-server 172.20.0.11:9092 --topic my_data",
		"server3": "~/app/kafka/kafka_2.13-3.6.2/bin/kafka-console-consumer.sh --bootstrap-server 172.20.0.12:9092 --topic my_data"
	}

	tasks = []
	for server, command in commands.items():
		tasks.append(run_command(server, command))

	await asyncio.gather(*tasks)

asyncio.run(main())
