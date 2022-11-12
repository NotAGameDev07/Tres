import socket, time

HOST = "::"
PORT = 32768

with socket.socket(socket.AF_INET6, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT))
	s.listen(1500)
	conn, addr = s.accept()
	with conn:
		print(f"Connected to {addr}")
		while True:
			data = conn.recv(1024)
			print(data)
			if not data:
				break
			time.sleep(10)
			conn.sendall(data)