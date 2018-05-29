#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 函数的参数

# 1. 默认参数
def my_power(x, n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(my_power(3))
print(my_power(3, 4))

# 默认参数一定要用不可变对象

# 2. 可变参数

def my_sum(*numbers):
    '''
    计算立方和
    '''
    sum = 0
    for n in numbers:
        sum += n ** 3
    return sum

print('my_sum = %s' % my_sum(1, 3, 5, 9))

# 3. 关键字参数
def my_person(name, age, **kw):
    print(name, age, kw)

my_person('Martin', 22, sex='男', height=181)

# 4. 命名关键字参数

def my_user(name, age, *, city, job):
    print(name, age, city, job)

my_user('Martin', 22, city='Wuxi', job='Manong')
# my_user('Martin', 22, city='Wuxi', job='Manong', height=181) # 会报错
