#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# class FooBar(object):
#     def __init__(self, value=42):
#         '''
#         构造函数
#         '''
#         self.somevar = value
#     def __del__(self):
#         '''
#         析构函数
#         在对象被GC前运行，尽量别用，因为我们不知道什么时候运行GC。
#         '''
#         print('Byebye!')

# f = FooBar(66)
# print(f.somevar)
# f = FooBar('a quick brown fox')
# print(f.somevar)
# f = None


# class A(object):
#     def hello(self):
#         print("Hello, I'm A.")


# class B(A):
#     pass


# class C(A):
#     def hello(self):
#         print("Hello, I'm C.")


# a = A()
# b = B()
# c = C()
# a.hello()  # Hello, I'm A.
# b.hello()  # Hello, I'm A.
# c.hello()  # Hello, I'm C.

# class Bird(object):
#     def __init__(self):
#         self.hungry = True

#     def eat(self):
#         if self.hungry:
#             print('Aaaaaah...')
#             self.hungry = False
#         else:
#             print('No, thanks!')


# class SongBird(Bird):
#     def __init__(self):
#         super().__init__()
#         self.sound = 'Squawk!'

#     def sing(self):
#         print(self.sound)


# b = Bird()
# b.eat()

# sb = SongBird()
# sb.sing()
# sb.eat()








class Employee(object):
    def __init__(self, username, age):
        self.username = username
        self.age = age
    
    def __getattribute__(self, attr):
        return super(Employee, self).__getattribute__()

    










# def check_index(key):
#     if not isinstance(key, int):
#         raise ValueError
#     if key < 0:
#         raise IndexError


# class ArithmeticsSequence(object):
#     def __init__(self, start=0, step=1):
#         self.start = start
#         self.step = step
#         self.changed = {}

#     def __getitem__(self, key):
#         '''
#         从算术序列中获取一个元素
#         '''
#         check_index(key)
#         try:
#             return self.changed[key]
#         except KeyError:
#             return self.start + key * self.step

#     def __setitem__(self, key, value):
#         check_index(key)
#         self.changed[key] = value

# s = ArithmeticsSequence(1, 2)
# print(s[4])
# print(s[12])
# print(s[111])
# print(s[12332])
