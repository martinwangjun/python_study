#!/usr/bin/python
# -*- coding: utf-8 -*-

import time


def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


start = time.time()
print(fib(800))
end = time.time()
duration = end - start
print('Duration: %.6f' % duration)
