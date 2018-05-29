#!/usr/bin/python
# -*- coding: utf-8 -*-

# 输出指定范围内的素数
import math

# lower = int(input("Min: \n"))
# upper = int(input("Max: \n"))

# for num in range(lower, upper + 1):
#     if num > 1:
#         for i in range(2, int(math.sqrt(num)) + 1):
#             if num % i == 0:
#                 break
#         else:
#             print(num)


lower = 2
upper = 100


def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


for i in range(lower, upper + 1):
    if is_prime(i):
        print(i)
