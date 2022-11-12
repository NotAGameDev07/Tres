import socket

HSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
	csock, addr = s.accept()
	print(f"CONN from {addr} has been established")
	msg = "WELCOME"
	msg = f'{len(msg):<{HSIZE}}' + msg
	csock.send(bytes(msg, 'utf-8'))
	csock.close()