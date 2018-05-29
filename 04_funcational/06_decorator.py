#!/usr/bin/env python
# -*- coding: utf-8 -*-


def now():
    print('2017-6-29')

f = now
f()

# 函数也是对象，函数对象有个__name__属性
print(now.__name__)
print(f.__name__)


def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper


@log
def now():
    print('2017-6-29')

now()
