#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict

def test():
    return 'N/A'

# dd = defaultdict(test)
dd = defaultdict(lambda: 'N/A')
dd['k1'] = 'ABC'
print(dd['k1'])
print(dd['k2'])
