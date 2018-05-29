#!/usr/bin/python
# -*- coding: utf-8 -*-

# 定义一个Exception类，继承自ValueError
# @see https://docs.python.org/3/library/exceptions.html#exception-hierarchy


class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n


# 捕获错误FooError
try:
    foo('0')
except FooError as err:
    print(err)
