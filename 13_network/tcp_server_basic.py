#!/usr/bin/python
# -*- coding: utf-8 -*-

# 服务器端
import socket, threading, time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 9876

# 绑定监听端口
s.bind((SERVER_HOST, SERVER_PORT))
s.listen(5)
print('Waiting for connection...')

def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

while True:
    sock, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()


