#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import StringIO
f = StringIO()
qty = f.write('Hello World')
print(qty)

f = StringIO('a\nquick\nbrown\nfox\njumps\nover\na\nlazy\ndog.')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
