#!/usr/bin/python
# -*- coding: utf-8 -*-

# 读取/写入一个二进制文件
s = ''
with open('01_linux.jpg', 'rb') as f:
    s = f.read()
with open('02.jpg', 'wb') as f:
    f.write(s)

with open('dump.txt', 'rb') as f:
    s = f.read()
    print(s)
    print(s.decode('utf-8'))
with open('dump2.txt', 'wb') as f:
    f.write(s)
