#!/usr/bin/env python
# -*- coding: utf-8 -*-
import functools


def begin_end_call(f):
    @functools.wraps(f)
    def wrapper(*args, ** kw):
        print('begin call')
        g = f(*args, ** kw)
        print('end call')
        return g
    return wrapper


@begin_end_call
def foo(bar):
    print(bar)

foo('111')
