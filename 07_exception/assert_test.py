#!/usr/bin/python
# -*- coding: utf-8 -*-

def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    print(foo(0))

main()