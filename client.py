import socket
import pickle

HSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect((socket.gethostname(), 1234))

while True:
    full_msg = b''
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            print(f"new message length: {msg[:HSIZE]}")
            try:
                msglen = int(msg[:HSIZE])
            except:
                msglen = 0
            new_msg = False
        full_msg += msg
        if len(full_msg) - HSIZE == msglen:
            print("full msg recvd")
            print(full_msg[HSIZE:])

            d = pickle.loads(full_msg[HSIZE:])
            print(d)

            new_msg = True
            full_msg = b''

    print(full_msg)