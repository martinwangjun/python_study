#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# # 使用dict函数来生成一个map的正确方式
# items = [('name', 'Gumby'), ('age', 42)]
# d = dict(items)
# print(d)  # {'name': 'Gumby', 'age': 42}

# d = dict(name='Alice', age=12)
# print(d)  # {'name': 'Alice', 'age': 12}

# d = {
#     'name': 'Teddy',
#     'age': 12,
#     'score': 99
# }
# print(d)  # {'name': 'Teddy', 'age': 12, 'score': 99}


# d = {
#     'name': 'Teddy',
#     'age': 12,
#     'score': 99
# }

# # 返回键值对的对数
# print(len(d))  # 3
# # 返回age对应的值
# print(d['age'])  # 12
# # 设置score的值
# d['score'] = 100  # {'name': 'Teddy', 'age': 12, 'score': 100}
# print(d)
# # 添加一个height键的值
# d['height'] = 171  # {'name': 'Teddy', 'age': 12, 'score': 100, 'height': 171}
# print(d)
# # 删除键值height
# del d['height']
# print(d)  # {'name': 'Teddy', 'age': 12, 'score': 100}
# # in用于检测k是否在dict中
# print('age' in d)  # True
# print('height' in d)  # False

d = {
    'name': 'Teddy',
    'age': 12,
    'score': 99
}

d.clear()
print(d)  # {}

x = {
    'name': 'Teddy',
    'age': 12,
    'score': 99
}
y = x.copy()
print(x)
print(y)
x.clear()
print(x)  # {'name': 'Teddy', 'age': 12, 'score': 99}
print(y)  # {'name': 'Teddy', 'age': 12, 'score': 99}

# 3. fromkeys
d = {}.fromkeys(['name', 'age'])
print(d)  # {'name': None, 'age': None}
d = {}.fromkeys(['name', 'age'], '12')
print(d)  # {'name': '12', 'age': '12'}


# 4. get
# 键不存在的话，get不会抛出异常，而且可以设置默认值
d = {}
print(d.get('name'))
print(d.get('name', 'Default Value'))


# 5. items
d = {
    'name': 'Teddy',
    'age': 12,
    'score': 99
}
items = d.items()  # dict_items([('name', 'Teddy'), ('age', 12), ('score', 99)])
print(items)
for x in items:
    print(x)




