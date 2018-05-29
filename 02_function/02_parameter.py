#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 默认参数


def power(x, n=2):
    """默认参数"""
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(5, 6))
print(power(5))


def enroll(name, gender, age=6, city='Shanghai'):
    s = {
        'name': name,
        'gender': gender,
        'age': age,
        'city': city
    }
    return s

# 各种调用不同的默认参数
print(enroll('Miffy', 'F'))
print(enroll('Alice', 'F', 7))
print(enroll('Rebecca', 'F', 5, 'Lundon'))
print(enroll('George', 'M', city='Beijing'))

# 默认参数如果使用了“可变对象”，就会有个巨坑！！！


def foo(bar=[]):
    bar.append('BAR')
    return bar

# 正常情况下没什么
print(foo([1, 2, 3]))
print(foo(['A', 'B', 'C']))

# 使用默认参数呢？
print(foo())
print(foo())
print(foo())


def foo_dic(k, v, bar={}):
    bar[k] = v
    return bar

print(foo_dic('a', 1))  # 运行结果： {'a': 1}
print(foo_dic('b', 2))  # 运行结果： {'a': 1, 'b': 2}，而不是{'b': 2}
# 所以，不要用可变对象做默认参数，否则坑死你

# 避坑


def foo_work_well(bar=None):
    if bar is None:
        bar = []
    bar.append('BAR WORK WELL')
    return bar

print(foo_work_well())
print(foo_work_well())
print(foo_work_well())

# 可变参数


def sum_normal(li):
    """可变参数用tuple or list传入"""
    s = 0
    for x in li:
        s = s + x
    return s

print(sum_normal([1, 2, 3, 4, 5]))


def sum_super(*item):
    """可变参数用可变参数传入"""
    s = 0
    for x in item:
        s = s + x
    return s

print(sum_super(1, 2, 3, 4, 5))

# 如果参数已经是一个tuple/list了，怎么办？
a_param_tuple = (2, 3, 4, 5, 6)
a_param_list = [2, 3, 4, 5, 6]
print(sum_super(*a_param_tuple))
print(sum_super(*a_param_list))

# 关键字参数


def person(name, age, **kw):
    """可以传入任意多的参数"""
    print('name: %s age: %d other: %s' % (name, age, kw))

person('Charley', 14, city='Shanghai', title='Manager')

# 参数组合
