# https://www.codewars.com/kata/integers-recreation-one/train/python

# Divisors of 42 are : 1, 2, 3, 6, 7, 14, 21, 42. These divisors squared are: 
# 1, 4, 9, 36, 49, 196, 441, 1764. The sum of the squared divisors is 2500 
# which is 50 * 50, a square!

# Given two integers m, n (1 <= m <= n) we want to find all integers between 
# m and n whose sum of squared divisors is itself a square. 
# 42 is such a number.

# The result will be an array of arrays or of tuples (in C an array of Pair) 
# or a string, each subarray having two elements, first the number whose 
# squared divisors is a square and then the sum of the squared divisors.

# #Examples:

# list_squared(1, 250) --> [[1, 1], [42, 2500], [246, 84100]]
# list_squared(42, 250) --> [[42, 2500], [246, 84100]]
# The form of the examples may change according to the language, 
# see Example Tests: for more details.

# Note

# In Fortran - as in any other language - the returned string is not permitted
#  to contain any redundant trailing whitespace: you can use dynamically 
# allocated character strings.

# from math import sqrt
# def list_squared(m, n):
#   squared_list = []
#   for x in range(m, n + 1):
#     fact_list = []
#     s = 0
#     for i in range(1, x + 1):
#       if x % i == 0:
#         fact_list.append(i)
#         s += i ** 2
#     if sqrt(s) == int(sqrt(s)):
#       squared_list.append([x, s])
#   return squared_list

import time

from math import sqrt
def list_squared(m, n):
  squared_list = []
  for x in range(m, n + 1):
    fact_list = set()
    s = 0
    i = 1
    j = 0
    y = x
    while i <= int(sqrt(y)):
      if y % i == 0:
        z = y // i
        fact_list.add(i)
        fact_list.add(z)
      i += 1
      j += 1
    s = sum(map(lambda x: x ** 2, fact_list))
    if sqrt(s) == int(sqrt(s)):
      squared_list.append([x, s])
  return squared_list


def list_squared2(m, n):
  final = []
  for i in range(m, n+1):
    results = []
    for j in range(1, int(sqrt(i))+1):
      if i % j == 0:
        if int(i / j) != j:
          results.append(int(i / j) ** 2)
        results.append(j ** 2)
    summ = sum(results)
    if (sqrt(summ).is_integer()):
      final.append([i, summ])
  return final

t0 = time.time()

print(list_squared(1, 250))
print(list_squared(42, 250))
print(list_squared(250, 500))

t1 = time.time()
print(int((t1 - t0) * 10000))

print(list_squared2(1, 250))
print(list_squared2(42, 250))
print(list_squared2(250, 500))

t2 = time.time()
print(int((t2 - t1) * 10000))

# Test.assert_equals(list_squared(1, 250), [[1, 1], [42, 2500], [246, 84100]])
# Test.assert_equals(list_squared(42, 250), [[42, 2500], [246, 84100]])
# Test.assert_equals(list_squared(250, 500), [[287, 84100]])
