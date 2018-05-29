#!/usr/bin/env python
# -*- coding: utf-8 -*-

L = ['China', 'UK', 'USA', 'Russia', 'France']

# 切片
print(L[0:3])   # 取前三
print(L[:3])    # 取前三
print(L[-2:])   # 取倒数2个
print(L[::-1])  # 对L进行倒序

L1 = range(1, 101)  # 1-100
print(L1[4::5])     # 每5个，5, 10, 15, ...
print(L1[::-5])     # 每5个倒数，100, 95, 90, ...

# 字符串
s = 'calculation'
print(s[1:2])
print(s[::-1])      # 倒序

