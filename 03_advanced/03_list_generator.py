#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 列表生成式

## 生成平方
L1 = [x * x for x in range(1, 11)]
print(L1)

## 偶数的平方
L2 = [x * x for x in range(1, 11) if x % 2 == 0]
print(L2)

## 3的倍数的立法
L3 = [x ** 3 for x in range(1, 11) if x % 3 == 0]
print(L3)

## 生成全排列
L4 = [m + n for m in 'ABC' for n in 'WXYZ']
print(L4)

## 对数字补零
L5 = [('00' + str(x))[-3:] for x in range(1, 11)]
print(L5)

## 大小写转化
L6 = [s.lower() if isinstance(s, str) else s for s in ['Hello', 'World', 18, 'Apple', None]]
print(L6)
