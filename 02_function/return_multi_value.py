#!/usr/bin/python
# -*- coding: utf-8 -*-
import math

# 求解一元二次方程
def quadratic(a, b, c):
    delta = b * b - 4 * a * c
    x1, x2 = 0, 0
    if delta > 0:
        x1 = (-b + math.sqrt(delta))/(2 * a)
        x2 = (-b - math.sqrt(delta))/(2 * a)
    else:
        x1 = (-b + math.sqrt(-delta)*(1j))/(2 * a)
        x2 = (-b - math.sqrt(-delta)*(1j))/(2 * a)
    return x1, x2

print(quadratic(1, 1, 1))
