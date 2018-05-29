#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import time
import functools


def bar_time(msg=''):
    def foo_time(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            print(msg + " " + str(datetime.datetime.now()))  # 先执行打印时间，然后再执行功能
            time.sleep(1)
            return f(*args, **kwargs)
        return wrapper      # 最后返回这个包装函数
    return foo_time


@bar_time('Hello')
def bar(bar_str):
    print("bar " + bar_str)


@bar_time()
def bar2(bar_str):
    print("bar2 " + bar_str)

bar('bar')
bar2('bar2')

print(bar.__name__)
