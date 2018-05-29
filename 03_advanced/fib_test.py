#!/usr/bin/python
# -*- coding: utf-8 -*-

# def gen(n):
#     print('Hello World!')
#     yield 1 + n
#     yield 2 + n
#     yield 3 + n

# # for x in gen():
# #     print(x)
# g = gen(10)
# print(next(g))
# print(g.send(1000))
# print(next(g))


def MyGenerator():  
    value = (yield 1)  
    value = (yield value)  
    value = (yield value)  
    value = (yield value)  
    value = (yield value)  
  
  
gen = MyGenerator()  
print(next(gen))
print(next(gen))
# gen.close() # close()方法就是放弃了后面的yield
print(gen.send(20))
print(gen.send(13))
print(next(gen))

