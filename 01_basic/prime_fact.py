#!/usr/bin/env python
# -*- coding: utf-8 -*-

def fact(n):
    '''分解质因数'''
    print('{} = '.format(n), end="")
    if n in [1]:
        print('{}'.format(n))
    while n not in [1]:
        for i in range(2, n + 1):
            if n % i == 0:
                n = n // i
                if n == 1:
                    print(i)
                else:
                    print('{} *'.format(i), end=" ")
                break

n = int(input("Please enter an integer(>0): \n"))
fact(n)
