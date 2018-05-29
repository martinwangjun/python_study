#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function


class Student(object):
    """Student is a class"""
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))


bart = Student('Bart', 50)
bart.print_score()
