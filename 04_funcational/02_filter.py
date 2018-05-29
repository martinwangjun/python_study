#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_odd(x):
    return x % 2 == 1

L0 = range(1, 101)
L1 = filter(is_odd, L0)
print(L1)


def is_prime(x):
    flag = 1
    if x == 1:
        flag = 0
    for y in range(2, x / 2 + 1):
        if x % y == 0:
            flag = 0
    return flag

L2 = filter(is_prime, L0)
print(L2)
