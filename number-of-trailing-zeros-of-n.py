# https://www.codewars.com/kata/number-of-trailing-zeros-of-n/discuss
# from math import log
# def zeros(n):
#   s = 0
#   # for i in range(1, n+1, 5):
#   #   s += facts_of_five(i)
#   for i in range(0, n, 5):
#     if i != 0:
#       s += int(log(n)/log(5))
#   return s

def zeros(n):
  if n <= 0:
    return 0
  s = 0
  while n != 0:
    s += n // 5
    n = n // 5
  return s
print(zeros(12332454324242))