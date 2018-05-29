#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def f(x):
    return x * x


# map的语法结构： map(function, iterable, ...)
r = map(f, [1, 2, 3])
print(list(r))
# 运行结果： [1, 4, 9]

# 使用内置的函数
r = map(len, ['martin', 'linda', 'nina'])
print(list(r))
# 运行结果： [6, 5, 4]

# 多个序列
l1 = [1, 3, 5, 7, 9]
l2 = (2, 4, 6, 8, 10)
r = map(lambda x, y: x * y, l1, l2)
print(list(r))
# 运行结果： [2, 12, 30, 56, 90]
