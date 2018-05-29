#!/usr/bin/env python
# -*- coding: utf-8 -*-

L0 = [x for x in range(1, 31) if x % 2 == 1]
print(L0)

L1 = map(lambda x: x * x, L0)
print(L1)

# lambda表达式在javascript里就是匿名函数function(){...}
# 或者就是javascript的 “=>” 表达式
# 不过在python里，匿名函数太弱了。
