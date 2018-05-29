# https://www.codewars.com/kata/youre-a-square/train
from math import sqrt

def is_square(n):    
  return False if n < 0 else int(sqrt(n)) == sqrt(n)

# test.describe("is_square")
# test.it("should work for some examples")
# test.assert_equals(is_square(-1), False, "-1: Negative numbers cannot be square numbers")
# test.assert_equals(is_square( 0), True, "0 is a square number")
# test.assert_equals(is_square( 3), False, "3 is not a square number")
# test.assert_equals(is_square( 4), True, "4 is a square number")
# test.assert_equals(is_square(25), True, "25 is a square number")
# test.assert_equals(is_square(26), False, "26 is not a square number")
