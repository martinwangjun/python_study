#!/usr/bin/python
# -*- coding: utf-8 -*-

# 猜数字游戏

import random
num = random.randint(1, 100)

while True:
    s = input('Please enter a number: \n')
    if s == 'QUIT':
        break
    s = int(s)
    if s > num:
        print('too big')
    elif s < num:
        print('too small')
    else:
        print("Win! The number is %d" % num)
        break
