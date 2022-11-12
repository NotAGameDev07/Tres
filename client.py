import socket
TCP_IP = "::"
TCP_PORT = 32768
BUFFER_SIZE = 1024
MESSAGE = b"Hello, World!"
s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.sendall(MESSAGE)
data = s.recv(BUFFER_SIZE)
print("received data:", data)
s.sendall(MESSAGE * 2)
data = s.recv(BUFFER_SIZE)
print("received data:", data)
s.close()