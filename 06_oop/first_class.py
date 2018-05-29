#!/usr/bin/python
# -*- coding: utf-8 -*-


class Student(object):
    pass

bart = Student()
bart.name = 'Bart'

def p(std):
    print(std.name)

bart.print_name = p

bart.print_name


