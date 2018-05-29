# -*- coding: utf-8 -*-

# dict
d = {
    'Guangdong': 75000,
    'Jiangsu': 72000,
    'Shandong': 60000
}

## 获取数据
print(d['Guangdong'])
print(d.get('Henan'))
print(d.get('Henan', 1))
print('Hebei' in d)

## 插入数据
d['Liaoning'] = 35000
print(d)

## 修改数据
print(d['Jiangsu'])
d['Jiangsu'] = 72500
print(d)

## 删除数据
d.pop('Shandong')
print(d)

# set
s = set([1, 2, 3, 2, 1])
print(s)

## 增加数据
s.add(5)
print(s)

## 删除数据
s.remove(5)
print(s)

## 两个集合的交集和并集
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
s3 = s1 & s2    # 交集
s4 = s1 | s2    # 并集
print(s3)
print(s4)
