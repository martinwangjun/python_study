#!/usr/bin/env python
# -*- coding: utf-8 -*-

L1 = [x * x for x in range(1, 11)]
print(L1)

# 创建一个生成器
g = (x * x for x in range(1, 11))
# 不要用.next()
print(g.next())
print(g.next())
print(g.next())
print(g.next())

for n in g:
    print n

# 斐波那契数列


def fib(max):
    """斐波那契数列生成器"""
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

for n in fib(10):
    print(n)




