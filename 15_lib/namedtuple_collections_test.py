#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 定义一个点，并且计算两点之间的距离

from collections import namedtuple
from math import sqrt
Point = namedtuple('Point', ['x', 'y'])
p1 = Point(0, 0)
p2 = Point(1, 1)
l = sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)
print(l)
