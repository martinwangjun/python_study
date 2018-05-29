#!/usr/bin/python
# -*- coding: utf-8 -*-

# try:
#     r = 10 / 0
# except ZeroDivisionError as err:
#     print(err)
# finally:
#     print('finally')

# print('end')

# class MuffledCalculator:
#     muffled = True
#     def calc(self, expr):
#         try:
#             return eval(expr)
#         except ZeroDivisionError:
#             if self.muffled:
#                 print('Division by zero is illegal!')
#             else:
#                 raise

# mc = MuffledCalculator()
# print(mc.calc('10 / 2'))
# print(mc.calc('10 / 0'))

# try:
#     x = int(input('Enter the first number: '))
#     y = int(input('Enter the second number: '))
#     print(x / y)
# except ZeroDivisionError:
#     print("The second number can't be zero.")
# except ValueError:
#     print("That wasn't a number, was it?")

# while True:
#     try:
#         x = int(input('Enter the first number: '))
#         y = int(input('Enter the second number: '))
#         print(x / y)
#     except (ZeroDivisionError, ValueError) as ex:
#         print("Please enter a legal number.")
#         print(ex)
#     else: # 没有引发异常
#         break

try:
    x = int(input('Enter the first number: '))
    y = int(input('Enter the second number: '))
    print(x / y)
except ZeroDivisionError:
    print("The second number can't be zero.")
except ValueError:
    print("That wasn't a number, was it?")
finally:
    print('Finally!')
