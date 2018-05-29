#!/usr/bin/python
# -*- coding: utf-8 -*-

import time


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        a, b = b, a + b
        n = n + 1
    return a


start = time.time()
print(fib(800))
end = time.time()
duration = end - start
print('Duration: %.6f' % duration)
