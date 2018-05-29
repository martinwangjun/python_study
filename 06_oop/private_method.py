#!/usr/bin/env python#
# -*- coding: utf-8 -*-

class Secretive(object):
    def __inaccessible(self):
        print("Bet you can't see me ...")
    def accessible(self):
        print("The secret message is:")
        self.__inaccessible()

s = Secretive()
s._Secretive__inaccessible() # 运行结果： Bet you can't see me ...
