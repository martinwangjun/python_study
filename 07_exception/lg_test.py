#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
logging.basicConfig(level=logging.INFO)
# logging 对应的级别可以参考java的logging的参数

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
