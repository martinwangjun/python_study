#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

def fib(number):
    if number == 0 or number == 1:
        return 1
    else:
        return fib(number - 1) + fib(number - 2)

print(fib(25))
