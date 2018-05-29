#!/usr/bin/python
# -*- coding: utf-8 -*-

# This python program shows how to read a text file in correct encoding.
# readme.txt file is a utf-8 encoding text file.

# 1. read text file
# f = open('readme.txt', 'r', encoding='utf-8')
# s = f.read()
# f.close()
# print((s))

# f = None
# try:
#     f = open('readme.txt', 'r', encoding='utf-8')
#     print(f.read())
# finally:
#     if f:
#         f.close()

with open('./readme.txt', 'r', encoding='utf-8') as f:
    print(f.read())
