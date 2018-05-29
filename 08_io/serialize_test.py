#!/usr/bin/python
# -*- coding: utf-8 -*-

import pickle
import json
d = dict(
    name='张二狗',
    age=20,
    score=99)
with open('dump.txt', 'wb') as f:
    pickle.dump(d, f)
with open('dump_json.txt', 'w') as f:
    json.dump(d, f)
