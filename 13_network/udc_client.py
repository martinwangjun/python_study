#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

HOST = '127.0.0.1'
PORT = 8848

for data in [b'Linda', b'Rebecca', b'Sunny']:
    # 发送数据
    s.sendto(data, (HOST, PORT))
    # 接收数据
    print(s.recv(1024).decode('utf-8'))

s.close()
