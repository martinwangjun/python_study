# -*- coding: utf-8 -*-

# list

## 定义一个list，包含3个城市
cities = ['Beijing', 'Shanghai', 'Guangzhou']
print(cities)
print(len(cities))

## 取得list中的元素
print(cities[0])    # 获取第一个元素
# print(cities[3])  # 会报错，下标越界
print(cities[-1])   # 获取最后一个元素

## 增删改元素

### 增
cities.append('Chongqing')      # 在尾部添加一个元素 Chongqing
print(cities)
cities.insert(2, 'Shenzhen')    # 在第三个位置添加一个 Shenzhen
print(cities)

### 删
cities.pop()    # 删除最后一个元素
print(cities)
cities.pop(2)   # 删除指定位置元素
print(cities)

### 改
cities[2] = 'Tianjin'   # 修改指定位置元素
print(cities)

## tuple

t0 = ()         # 定义一个空的tuple
t1 = (1, )      # 定义一个1个元素的tuple，注意不能用t1 = (1)
t2 = (1, 2)     # 定义一个2个元素的tuple

print(t0)
print(t1)
print(t2)

## 混合
m = (1, 2, [3, 4])
m[2].append(5)
print(m)
