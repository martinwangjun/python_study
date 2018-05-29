#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Person(object):
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def greet(self):
        print('Hello, {}'.format(self.name))

p = Person()
p.set_name('张飞')
p.greet()
