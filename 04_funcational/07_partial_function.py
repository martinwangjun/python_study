#!/usr/bin/env python
# -*- coding: utf-8 -*-
import functools

print(int('10101'))
print(int('10101', base=2))


# def int2(x, base=2):
#     return int(x, base)

int2 = functools.partial(int, base=2)
print(int2('10101'))
