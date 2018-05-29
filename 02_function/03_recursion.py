#!/usr/bin/env python
# -*- coding: utf-8 -*-


def fact(n):
    """利用递归计算阶乘"""
    if n == 1:
        return 1
    return n * fact(n - 1)

print(fact(100))

# 尾递归优化, Python不行哦


def fact1(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print(fact1(1000))
