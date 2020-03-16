# Name:echo-client
# Author:Yasu
# Time:2020/3/16

import socket

Host = '127.0.0.1'
Port = 6500

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((Host,Port))
    sock.sendall(b'Hello World!')
    data = sock.recv(1024)

print('Received!', repr(data))