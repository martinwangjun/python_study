#!/usr/bin/python
# -*- coding: utf-8 -*-

L1 = list(x * x for x in range(1, 11) if x % 2 == 0)
print('L1 = ', L1)
L1 = [x * x for x in range(1, 11)]
print('L1 = ', L1)

L2 = list(m + n for m in 'ABC' for n in 'XYZ')
print('L2 = ', L2)

# import os
# L3 = list(d for d in os.listdir('..'))
# print('L3 = ', L3)

L4 = ['martin', 'rebecca', 'miffy', 12]
L4 = list(s.title() for s in L4 if isinstance(s, str))
print('L4 = ', L4)