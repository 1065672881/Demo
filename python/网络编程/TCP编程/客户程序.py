import socket, threading
import time

s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.connect(('127.0.0.1', 9999))
print(s1.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Tracy', b'Sarah']:
    s1.send(data)
    print(s1.recv(1024).decode('utf-8'))
s1.send(b'exit')
s1.close()
