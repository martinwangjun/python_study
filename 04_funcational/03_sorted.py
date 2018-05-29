#!/usr/bin/env python
# -*- coding: utf-8 -*-


def desc_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0

L0 = [36, 5, 12, 9, 21]
print(sorted(L0))               # 排序
print(sorted(L0, desc_cmp))     # 逆排序

L1 = ['bob', 'about', 'Zoo', 'Credit']
print(sorted(L1))               # 默认按照字母的ASCII排序


def cmp_ignore_case(s1, s2):
    l1 = s1.lower()
    l2 = s2.lower()
    if (l1 < l2):
        return -1
    elif (l1 > l2):
        return 1
    else:
        return 0

print(sorted(L1, cmp_ignore_case))  # 按照字母的ASCII排序，不区分大小写
