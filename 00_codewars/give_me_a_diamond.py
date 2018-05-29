# https://www.codewars.com/kata/give-me-a-diamond/train

def diamond(n):
  if n < 1 or n % 2 == 0:
    return None
  s = ''
  for i in range(0, n):
    s += ' ' * abs((n - 2 * i - 1) // 2) + '*' * (n - 2 * abs(i + 1 - (n + 1) // 2)) + '\n'
  return s

print(diamond(15))

# expected =  " *\n"
# expected += "***\n"
# expected += " *\n"
# test.assert_equals(diamond(3), expected)

