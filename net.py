import pickle
import socket


class Network:
	def __init__(self, ip, port, hsize=10):
		self.HSIZE = hsize
		self.ip = ip
		self.port = port
		self.con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.con.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
	def connect(self):
		try:
			self.con.connect((self.ip, self.port))
			print("[CONN EST]")
			return self.con
		except:
			print("[CONN ERR]")
	
	def host(self):
		try:
			self.con.bind((self.ip, self.port))
			print("[SERVER STARTED]")
			return self.con
		except:
			print("[ERROR]")
	
	def send(self, con, data):
		msg = pickle.dumps(data)
		msg = bytes(f'{len(msg):<{self.HSIZE}}', 'utf-8') + msg
		con.send(msg)
	
	def recv(self):
		full_msg = b''
		new_msg = True
		while True:
			msg = self.con.recv(16)
			if new_msg:
				print(f"new message length: {msg[:self.HSIZE]}")
				try:
					msglen = int(msg[:self.HSIZE])
				except:
					msglen = msglen
				new_msg = False
			if msg == b'':
				break
			full_msg += msg
			if len(full_msg) - self.HSIZE == msglen:
				print("full msg recvd")
				print(full_msg[self.HSIZE:])
				d = pickle.loads(full_msg[self.HSIZE:])
				print(d)
				new_msg = True
				full_msg = b''
		return d