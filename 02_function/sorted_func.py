#!/usr/bin/env python3
# -*- coding: utf-8 -*-

l = [12, -98, 23, -74, 65, 23, 53, -58, 12, -37, 7, 413]
print(sorted(l))
print(sorted(l, key=abs))
print(sorted(l, key=lambda x: abs(1/x)))
print(sorted(l, key=lambda x: abs(1/x), reverse=True))

# 运行结果：
# [-98, -74, -58, -37, 7, 12, 12, 23, 23, 53, 65, 413]
# [7, 12, 12, 23, 23, -37, 53, -58, 65, -74, -98, 413]
# [413, -98, -74, 65, -58, 53, -37, 23, 23, 12, 12, 7]
# [7, 12, 12, 23, 23, -37, 53, -58, 65, -74, -98, 413]