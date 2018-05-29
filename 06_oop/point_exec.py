#!/usr/bin/python
# -*- coding: utf-8 -*-
import math


class Point(object):
    '''Represent a point in two-dimensional geometric coordinates'''

    def __init__(self, x=0, y=0):
        '''Initialize the position of a new point. The x and y coordinates
        can be specified. If they are not, the point defaults to the origin.'''
        self.move(x, y)

    def move(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        self.x = 0
        self.y = 0

    def calculate_distance(self, other_point):
        return math.sqrt(
            (self.x - other_point.x) ** 2 +
            (self.y - other_point.y) ** 2
        )

# p1 = Point(0, 0)
# p2 = Point(3, 3)

# p2.move(3, 4)
# print(p1.calculate_distance(p2))
