#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 变量可以指向函数
print(abs(-100))    # 输出： 100
print(abs)          # <built-in function abs>
f = abs
print(f)
print(f(-10))

abs = 1314
print(abs)          # abs在这个时候已经变成100了
del abs             # 恢复abs的功能
print(abs(-5))

# 传入函数当参数


def add(x, y, f):
    """传入函数当参数"""
    return f(x) + f(y)

print(add(-3, -4, abs))

# map/reduce
## map
L0 = range(1, 10)
Lm1 = map(str, L0)
print(Lm1)


def double(x):
    return x * 2

Lm2 = map(double, L0)
print(Lm2)

## reduce


def add2(x, y):
    return 10 * x + y

Lr1 = reduce(add2, L0)
print(Lr1)

# 利用map和reduce

## 整理名字的首字母大写
LName = ['adam', 'LISA', 'barT']


def upper_first(s):
    return s[0].upper() + s[1:].lower()

LName1 = map(upper_first, LName)
print(LName1)

## 实现连乘
LNum = [3, 1, 4, 5, 9, 2, 7]


def multiply(x, y):
    return x * y

LNum1 = reduce(multiply, LNum)
print(LNum1)
