#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
# 创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
HOST = 'www.sina.com.cn'
PORT = 80
BUFF = 1024
s.connect((HOST, PORT))

# 发送数据
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 接收数据
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(BUFF)
    if d:
        buffer.append(d)
    else:
        break
    
data = b''.join(buffer)
s.close()
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
with open('sina.html', 'wb') as f:
    f.write(html)
