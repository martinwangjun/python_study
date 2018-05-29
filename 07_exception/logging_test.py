#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging

# 使用logging来记录出错的情况


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as err:
        logging.exception(err)


main()
print('END')
