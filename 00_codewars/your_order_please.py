# https://www.codewars.com/kata/your-order-please/train
import re

def order(sentence):
  return ' '.join(sorted(sentence.split(" "), key=lambda s: re.sub(r'\D', '', s)))

print(order("is2 Thi1s T4est 3a"))
# print(getnum('fdsf4dsf'))

# Test.assert_equals(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")
