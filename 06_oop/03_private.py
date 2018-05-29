#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

class Student(object):
    """Student is a class"""
    def __init__(self, name, score):
        self.__name = name  # 双下划线开头的变量表示私有变量
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def __calc_is_pass(self):
        if self.__score >= 60:
            print("Pass")
        else:
            print("Fail")

    def is_pass(self):
        self.__calc_is_pass()

bart = Student('Bart', 50)
bart.print_score()
# bart.__calc_is_pass()     # 私有方法，不能访问
bart.is_pass()
