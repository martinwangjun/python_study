#!/usr/bin/python
# -*- coding: utf-8 -*-


def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] consuming %s ...' % n)
        r = '200 OK'


def produce(c):
    c.send(None) # 效果与next(c)一样
    n = 0
    while n < 2:
        n = n + 1
        print('[PRODUCER] producing %s ...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s ...' % r)
    c.close()


c = consumer()
produce(c)
