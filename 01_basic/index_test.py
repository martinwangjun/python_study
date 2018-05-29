#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# s = 'Hello'

# # 索引
# print(s[0])

# database = [
#     ['albert', '1234'],
#     ['dilbert', '4242'],
#     ['smith', '7524'],
#     ['jones', '9843']
# ]

# username = input('User Name: ')
# pin = input('Pin: ')

# if [username, pin] in database:
#     print('Pass')
# else:
#     print('Access Denied!')

# print(len(database))

# l = list('Grape')
# print(l)
# print('-'.join(l))

# names = ['Alice', 'Beth', 'Cecil', 'Dee-Dee', 'Earl']
# del names[0]
# print(names)


# lst = [1, 2, 3]
# lst.append(4)
# print(lst)

# lst.clear()
# print(lst)

# a = [1, 2, 3]
# b = a
# b[0] = 0
# print('A: %s, B: %s' % (a, b))

# a = [1, 2, 3]
# b = a.copy()
# b[0] = 0
# print('A: %s, B: %s' % (a, b))

# a = [1, 2, 3]
# b = [4, 5, 6]
# print(a + b)
# print(a)

# a.extend(b)
# print(a)

# letters = list('a quick brown fox jumps over a lazy dog.')
# print(letters.count('a'))

x = [-3, 2, 9, 1, -4]
# 按绝对值排序，key可以是一个排序函数
x.sort(key=abs, reverse=True)
print(x)
# 按倒数排序，采用lambda表达式（匿名函数）来传入key
x.sort(key=lambda x: 1 / x, reverse=True)
print(x)
