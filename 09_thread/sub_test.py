#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

# 调用一个外部程序成为子进程
print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code: ', r)

print('$ nslookup')
