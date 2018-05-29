#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

# def student2dict(student):
#     return {
#         'name': student.name,
#         'age': student.age,
#         'score': student.score
#     }

s = Student('刘老六', 20, 99)
# print(json.dumps(s, default=student2dict))

# print(s.__dict__)
# print(json.dumps(s, default=lambda obj: obj.__dict__))


print(s.__class__.__base__)

#     }

s = Student('刘老六', 20, 99)
# print(json.dumps(s, default=student2dict))

# print(s.__dict__)
# print(json.dumps(s, default=lambda obj: obj.__dict__))


print(s.__class__.__base__)

