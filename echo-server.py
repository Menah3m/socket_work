# Name:echo-server
# Author:Yasu
# Time:2020/3/16

import socket

Host = '127.0.0.1'
Port = 6500

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    print('Socket Created!')

    sock.bind((Host, Port))
    print('Socket Bind Completed!')

    sock.listen(10)
    print('Socket listening...')

    conn, addr = sock.accept()
    with conn:
        print('Connected by',addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)








