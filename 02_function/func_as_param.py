#!/usr/bin/python
# -*- coding: utf-8 -*-

# 把abs作为参数传递给f
# f = abs
# print(f(-2))
def search(sequence, number, lower=0, upper=None):
    if upper is None: 
        upper = len(sequence) + 1
    if lower == upper:
        assert number == sequence[upper]
        return upper
    else:
        middle = (upper + lower) // 2
        if number > sequence[middle]:
            return search(sequence, number, middle + 1, upper)
        else:
            return search(sequence, number,lower, middle)


seq = [34, 67, 8, 123, 4, 100, 95]
seq.sort()

print(search(seq, 123))


