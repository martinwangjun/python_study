#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import copy

# 深Copy与浅Copy

a = [1, 2, 3, 4, 5]
b = ['A', 'B', a]
c = b[:]
d = copy.deepcopy(b)
print(c)
print(d)

a[0] = 111
print(c)
print(d)
