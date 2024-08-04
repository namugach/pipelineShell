# | hostname | ip | port |

class ServerInfo:
	def __init__(self, name, ip, port=2222) -> None:
		self.name = name
		self.ip = ip
		self.port = port
		pass

server_infos = [
	ServerInfo("server1", "172.31.14.186"),
	ServerInfo("server2", "172.31.1.229"),
	ServerInfo("server3", "172.31.10.99")
]
