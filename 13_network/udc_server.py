#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
HOST = '127.0.0.1'
PORT = 8848
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口
s.bind((HOST, PORT))

print('Bind UDP on %s ...' % PORT)

while True:
    # 接收数据
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    reply = 'Hello, %s!' % data.decode('utf-8')
    s.sendto(reply.encode('utf-8'), addr)
