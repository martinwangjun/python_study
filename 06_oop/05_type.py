#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import types

# 使用type()


print(type(123))
print(type('abc'))
print(type(None))


# 使用types里的枚举变量比较
print(type([]) == types.ListType)

# 使用isinstance()
print(isinstance('abc', str))


class Animal(object):
    """Animal Class"""
    def run(self):
        print('Animal is running.')

    def __len__(self):
        return 1100


class Dog(Animal):
    """Dog Class"""
    def run(self):
        print('Dog is running.')


class Husky(Dog):
    """Cat Class"""
    def run(self):
        print('Husky is running.')

animal = Animal()
dog = Dog()
husky = Husky()

print(isinstance(dog, Animal))
print(isinstance(husky, Animal))
print(isinstance(husky, Dog))

# 使用dir()函数了解一个对象的所有属性和方法
h = dir(husky)
print(h)

print(husky.__len__())
