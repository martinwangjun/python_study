#!/usr/bin/python
# -*- coding: utf-8 -*-

from io import StringIO, BytesIO

# StringIO
f = StringIO()
f.write('你好')
f.write(' ')
f.write('World!')
print(f.getvalue())

# str -> bytes: encode
# bytes -> str: decode

# BytesIO
b = BytesIO()
b.write('中文'.encode('utf-8'))
print(b.getvalue().decode('utf-8'))
