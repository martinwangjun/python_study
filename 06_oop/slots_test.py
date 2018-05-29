#!/usr/bin/python
# -*- coding: utf-8 -*-

class Student(object):
    pass

s1 = Student()
s2 = Student()

s1.name = 'Mike'
print(s1.name)


def set_score(self, score):
    self.score = score

Student.set_score = set_score # 给类绑定方法，会起作用
s1.set_score(10)
s2.set_score(20)
# print(s1.score)
# print(s2.score)

Student.school = '彭浦实验'
print(s1.school)
print(s2.school)


# 现在定义一个设置了__slots__的类
class Teacher(object):
    __slots__ = ('name', 'subject')

t1 = Teacher()
t1.name = 'Emma'
t1.subject = 'Maths'
# t1.age = 23 # 会报错的，age不在只读变量 __slots__ 里

class Trainer(Teacher):
    __slots__ = ('age') # Trainer类的__slots__就是这里的age加上它父类的__slots__

t2 = Trainer()
t2.name = 'Elsa'
t2.subject = 'Magic'
t2.age = 18
# t2.height = 167
