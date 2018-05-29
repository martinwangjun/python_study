#!/usr/bin/python
# -*- coding: utf-8 -*-

L = ['Ada', 'Betty', 'Candy', 'Daisy', 'Emily']
print(L[0::2])

str1 = '   abc   '
def trim(s):
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s
print(trim(str1))

