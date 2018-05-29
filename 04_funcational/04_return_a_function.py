#!/usr/bin/env python
# -*- coding: utf-8 -*-


def lazy_sum(*args):
    """返回一个函数"""
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(*range(1, 101))    # 高斯弟弟笑而不语

print(f())

# 闭包


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i ** 2
        fs.append(f)
    return fs
f1, f2, f3 = count()    # 这个时候i = 3了

print(f1())     # 结果是9
print(f2())     # 结果是9
print(f3())     # 结果是9

# 注意:
# 这个闭包和javascript的坑有得一拼，这种情况下调用不是同步的，是异步的！
# 熟悉javascript的小伙伴很容易搞懂
#
# 要避开这个坑，需要这样做：


def count2():
    fs = []
    for i in range(1, 4):
        def f(n):
            def g():
                return n ** 2
            return g
        fs.append(f(i))  # 这个时候，已经调用了f()，所以，这个时候会把i的值存入
    return fs
f1, f2, f3 = count2()

print(f1())     # 结果是1
print(f2())     # 结果是4
print(f3())     # 结果是9

# 在闭包里面，要注意什么时候调用了什么
