# https://www.codewars.com/kata/bit-counting/train

def countBits(n):
  print(str(bin(n)).count('1'))

# test.assert_equals(countBits(0), 0);
# test.assert_equals(countBits(4), 1);
# test.assert_equals(countBits(7), 3);
# test.assert_equals(countBits(9), 2);
# test.assert_equals(countBits(10), 2);

countBits(10)
