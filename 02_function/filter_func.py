#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def is_prime(n):
    if n == 1:
        return False
    for x in range(2, int(n / 2 + 1)):
        if n % x == 0:
            return False
    else:
        return True

l = [x for x in range(1, 101)]
print(list(filter(is_prime, l)))
