# -*- coding: utf-8 -*-

# 输出语句
a = 2
print(a ** 100)

# 格式化输出
# @link http://www.cnblogs.com/plwang1990/p/3757549.html
b = 3.54159265359
print('%d' % b)     # 取整数位输出，并没有四舍五入
print('%.2f' % b)   # 保留2位小数
print('%.4f' % b)   # 保留4位小数，四舍五入了
print('%.6f' % b)   # 保留6位小数，四舍五入了
print('%s' % b)     # 字符串方式输出

# 交换数值
c = 3
d = 4
print(c, d)
c, d = d, c
print(c, d)

print(12//10)