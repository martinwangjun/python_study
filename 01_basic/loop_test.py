#!/usr/bin/python
# -*- coding: utf-8 -*-

# # 显示单数
# for i in range(1, 100, 2):
#     if i % 20 == 1 and i != 1:
#         print("")
#     print(i, end="\t")
# print("")

# 数数，不含3，以及3的倍数
for i in range(1, 100):
    if i % 3 == 0 or str(i).count('3') > 0:
        continue
    print(i)
