# -*- coding: utf-8 -*-

a = -123
print(abs(a))

# 把abs这个函数的名字赋值给ab，ab就可以当成abs函数来用了，和javascript很像
ab = abs
print(ab(a))

# 把int赋值给abs，abs就可以当int()用
abs = int
print(abs(3.14))

# 使用del abs可以让失灵的abs恢复功能
del abs
print(abs(3.14))

# 定义函数


def my_abs(x):

    if x > 0:
        return x
    else:
        return -x

# 定义空函数


def do_nothing():
    pass

# 返回“多个值”，其实返回的是tuple啦


def move(x, y, step_x, step_y):
    nx = x + step_x
    ny = y + step_y
    return nx, ny

print(move(1, 1, 2, 2))
