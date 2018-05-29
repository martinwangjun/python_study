#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

# 在python中，我们可以方便的给一个对象绑定一个属性，如：


class Carrier(object):
    """Carrier 船的类别"""
    def __init__(self, name, cls):
        self.name = name
        self.cls = cls

    def get_info(self):
        return "Name: " + self.name + " Class: " + self.cls

liaoning = Carrier('Liaoning', '001')       # 辽宁号，级别是001型
liaoning.planes = 20                        # 舰载机20架

print(liaoning.get_info())
print(liaoning.planes)

# 现在我们要给辽宁号增加一个方法，launch_plane(qty)
# 使用MethodType就可以实现





