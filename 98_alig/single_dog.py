#!/usr/bin/python
# -*- coding: utf-8 -*-

# 故事背景和“单身狗”相同，只不过这次Party中混进了两只单身狗，请你输出这两只单身狗的编
# 号，小编号在前，大编号在后，以一个空格隔开。
# 例如：L=[1,1,4,4,3,5,5,7]
# 则输出：3 7

L = [1, 1, 4, 4, 3, 5, 5, 7, 3, 8]

def find_single(L):
    D = {}
    L2 = list()
    for n in L:
        if n not in D.keys():
            D[n] = 1
        else:
            D[n] = D[n] + 1
    for k, v in D.items():
        if v < 2:
            L2.append(str(k))
            L2.sort
    return ' '.join(L2)

print(find_single(L))