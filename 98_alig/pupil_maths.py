#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
MAX_RUN_COUNTER = 1000
# N以内的加减法运算


def plus_minus(max_number, hidden=False, max_qty=100):
    counter = 0
    operator = 0  # 0: '+', 1: '-'
    pool = set()
    while True:
        a = random.randint(21, max_number)
        b = random.randint(1, 10)
        c = a + b
        d = a - b
        operator = random.randint(0, 1)
        if operator == 0:
            if a + b <= max_number:
                if not hidden:
                    pool.add(str(a) + ' + ' + str(b) + ' = ')
                else:
                    if random.randint(0, 1) == 1:
                        pool.add(str(a) + ' + ' + '(    )' + ' = ' + str(c))
                    else:
                        pool.add('(    )' + ' + ' + str(b) + ' = ' + str(c))
        else:
            if a >= b:
                if not hidden:
                    pool.add(str(a) + ' - ' + str(b) + ' = ')
                else:
                    if random.randint(0, 1) == 1:
                        pool.add(str(a) + ' - ' + '(    )' + ' = ' + str(d))
                    else:
                        pool.add('(    )' + ' - ' + str(b) + ' = ' + str(d))
        if len(pool) > max_qty:
            break

        if counter > MAX_RUN_COUNTER:
            break
        counter += 1
    counter = 0
    pool = list(pool)
    while counter < max_qty:
        if counter % 4 == 3:
            print(pool[counter], end='\n')
        else:
            print(pool[counter], end='\t')
        counter += 1


if __name__ == '__main__':
    plus_minus(100)
