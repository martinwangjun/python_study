#!/usr/bin/env python
# -*- coding: utf-8 -*-

d = {'a': 1, 'b': 2, 'c': 3}
s = set([1, 2, 3])
l = [1, 3, 5, 7, 9]
str1 = 'abcdefg'

for key in d:
    print(key)

for value in d.itervalues():
    print(value)

for k, v in d.iteritems():
    print('%s => %s' % (k, v))

for key in s:
    print(key)

for key in l:
    print(key)

for key in str1:
    print(key)

# 判断是否是iterable对象

from collections import Iterable
print(isinstance('abc', Iterable))
print(isinstance(123, Iterable))

for i, value in enumerate(['A', 'B', 'C']):
    print('%s -> %s' % (i, value))

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)
