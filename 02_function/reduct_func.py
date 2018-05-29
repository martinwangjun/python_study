#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
r = reduce(lambda x, y: x*2+y*2, [1, 2, 3])
print(r)
