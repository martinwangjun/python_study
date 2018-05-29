#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

'''
python处理字符串
@version: 2.7.x
'''

# 字符串的切片
str_english = 'A quick brown fox jumps over a lazy dog.'
str_chinese = '有后悔的也不会在这告诉你啊。'
str_utf8 = u'最常用的数据类型'

print('-' * 50)

print("str_english[0]: %s" % str_english[0])
print("str_chinese[0]: %s" % str_chinese[1]) # 会无法显示
print("str_utf8[0]: %s" % str_utf8[0])

print('\n')

print("str_english[0:2]: %s" % str_english[0:2])
print("str_chinese[0:2]: %s" % str_chinese[0:2]) # 会显示乱码
print("str_utf8[0:2]: %s" % str_utf8[0:2])

print('-' * 50)

# 字符串运算符
s = str_english + str_utf8
print(type(s))
print(s)
print(str_english * 5)

print('-' * 50)

# 是否包含
print('jump' in str_english)
print('jump' not in str_english)

# 转移字符不起作用
print(r'\n')

# 格式化字符

# 内建函数
str_name = 'penny wang'
print(str_name.capitalize())
print(str_name.title())
print(str_name.count('n'))
