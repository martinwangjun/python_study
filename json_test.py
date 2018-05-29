#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
import json

data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]

json = json.dumps(data)
print(json)
