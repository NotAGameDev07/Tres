import socket
import pickle
import deck

HSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
	csock, addr = s.accept()
	print(f"CONN from {addr} has been established")
	msg = pickle.dumps(deck.Card)
	msg = bytes(f'{len(msg):<{HSIZE}}', 'utf-8') + msg
	csock.send(msg)
	csock.close()