#!/usr/bin/python
# -*- coding: utf-8 -*-

# # 列表与generator
# L = [x * x for x in range(1, 11)]
# G = (x * x for x in range(1, 11))

# print('L is a %s' % type(L)) # L is a <class 'list'>
# print('G is a %s' % type(G)) # G is a <class 'generator'>

# # 遍历list和generator
# for x in L:
#     print(x, end=' ')
# print('') # 显示结果: 1 4 9 16 25 36 49 64 81 100


# for x in G:
#     print(x, end=' ')
# print('') # 显示结果: 1 4 9 16 25 36 49 64 81 100

#######################################################
# 斐波那契数列
#######################################################

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     # return a

# for n in fib(10):
#     print(n)

# L = [1, 2, 3]
# L = iter(L)
# print(next(L))
# print(next(L))
# print(next(L))




# import time

# def func(n):
#     for i in range(0, n):
#         print('func: ', i)
#         yield i

# f = func(10)

# # print(func(10))

# while True:
#     print(next(f))
#     time.sleep(1)

import time, random
def func(n):
    for i in range(0, n):
        arg = yield i
        print('func: %s' % arg)

f = func(10)
while True:
    print('main: %s' % next(f))
    print('main: %s' % f.send(random.randint(1, 1000)))
    # print('main: %s' % f.send(None))
    time.sleep(1)


