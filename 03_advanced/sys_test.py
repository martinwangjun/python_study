#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
while True:
    response = input('Type EXIT to exit: \n')
    if response == 'EXIT':
        sys.exit(0)
    print('You typed ' + response + '.')
