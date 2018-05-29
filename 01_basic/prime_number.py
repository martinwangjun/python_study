#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
from math import sqrt
from sys import stdout

start = 100
end = 200

def is_prime(num):
    for i in range(2, int(sqrt(num))):
        if num % i == 0:
            return False
    return True

counter = 0
for i in range(start, end + 1):
    if is_prime(i):
        counter = counter + 1
        print(i, end=" ")

print("\n\nTotal: %d" % counter)
