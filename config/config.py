# | hostname | ip | port |

class ServerInfo:
	def __init__(self, id, name, ip, port=2222) -> None:
		self.id = id
		self.name = name
		self.ip = ip
		self.port = port
		pass

server_infos = [
	ServerInfo(1, "server1", "172.17.0.2"),
	ServerInfo(2, "server2", "172.17.0.3"),
	ServerInfo(3, "server3", "172.17.0.4")
]


# update_infos = [
# 	ServerInfo(1, "server1", "172.31.14.186"),
# 	ServerInfo(2, "server2", "172.31.10.99"),
# 	ServerInfo(3, "server3", "172.31.1.229")
# ]

update_infos = [
	ServerInfo(1, "server1", "server1"),
	ServerInfo(2, "server2", "server2"),
	ServerInfo(3, "server3", "server3")
]