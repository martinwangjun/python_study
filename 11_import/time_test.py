#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
now = datetime.now()
# 指定输出的日期格式
print('当前日期：%s' % now.strftime('%Y-%m-%d %H:%M:%S'))

# 生成一个指定的日期
dt = datetime(2011, 11, 11, 23, 59, 59)
print('生成日期：%s' % dt)

# timestamp
# Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。
print('时间戳：  %s' % now.timestamp())

# 日期加减
print(now + timedelta(days=10))
print(now - timedelta(days=-1))

