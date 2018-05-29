#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# formats = 'Hello, %s. %s enough for ya.'
# values = ('World', 'Hot')
# print(formats % values)

# from string import Template
# tmpl = Template("Hello $who! $what enough for ya.")
# print(tmpl.substitute(who='World', what='Dusty'))

# print("{}, {} and {}".format("first", "second", "third"))
# print( "{0}, {1} and {2}".format("first", "second", "third"))

# from math import pi
# p ="{name} is approximately {value:.2f}.".format(value=pi, name="π")
# print(p)

# print('{1}, {0}, {2}'.format('one', 'two', 'three'))

# width = int(input('Please enter width: '))
# price_width = 10
# item_width = width - price_width
# header_fmt = '{{:{}}}{{:>{}}}'.format(item_width, price_width)
# fmt = '{{:{}}}{{:>{}.2f}}'.format(item_width, price_width)
# print('=' * width)
# print(header_fmt.format('Item', 'Price'))
# print('-' * width)
# print(fmt.format('Apples', 0.4))
# print(fmt.format('Pears', 0.5))
# print(fmt.format('Cantaloupes', 1.92))
# print(fmt.format('Dried Apricots (16 oz.)', 8))
# print(fmt.format('Prunes (4 lbs.)', 12))
# print('=' * width)

import string
print(string.digits)

s = 'select'
# 实现居中，center有2个参数：长度和填充字符（默认是空格）
print(s.center(20, '*'))  # *******select*******

s = 'select'
print(s.center(20, '*'))
print(s.find('e'))  # 1
print(s.find('q'))  # -1
print(s.replace('e', 'E'))  # sElEct

s = 'select'
seq = list(s)
print(''.join(seq))  # select

s = 'yesterday once more'
seq = s.split(' ')
print(seq)  # ['yesterday', 'once', 'more']

s = '我的cPu很好'
print(s.upper())  # 我的CPU很好
print(s.lower())  # 我的cpu很好
print(s.title())  # 我的Cpu很好

s = '   a quick fat dog  '
print(s.strip())
print(s.strip())

# translate函数
table = str.maketrans('cs', 'kz')
trans = 'this is a crazy test'.translate(table)
print(trans)  # thiz iz a krazy tezt
table = str.maketrans('cs', 'kz', ' ')
trans = 'this is a crazy test'.translate(table)
print(trans)  # thizizakrazytezt

# capwords
s = 'this is an apple.'
print(string.capwords(s))
