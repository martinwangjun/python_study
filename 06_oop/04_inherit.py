#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function


class Animal(object):
    """Animal Class"""
    def run(self):
        print('Animal is running.')


class Dog(Animal):
    """Dog Class"""
    def run(self):
        print('Dog is running.')


class Cat(Animal):
    """Cat Class"""
    def run(self):
        print('Cat is running.')

dog = Dog()
dog.run()

cat = Cat()
cat.run()


def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(Dog())
run_twice(Cat())
