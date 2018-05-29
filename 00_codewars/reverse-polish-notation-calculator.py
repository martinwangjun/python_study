# https://www.codewars.com/kata/reverse-polish-notation-calculator/train
# @see https://en.wikipedia.org/wiki/Reverse_Polish_notation

def calc(expr):
  if expr == '': return 0
  expr = expr.split(' ')
  stack = []
  for x in expr:
    if x not in '+-*/':
      stack.append(float(x))
    else:
      b = float(stack.pop())
      a = float(stack.pop())
      if x == '+':
        stack.append(a + b)
      if x == '-':
        stack.append(a - b)
      if x == '*':
        stack.append(a * b)
      if x == '/':
        stack.append(a / b)
  return stack.pop()

  

print(calc(''))
print(calc('1 2 3'))
print(calc('1 2 3.5'))
print(calc('1 3 +'))
print(calc('1 3 *'))
print(calc('1 3 -'))
print(calc('4 2 /'))
print(calc('5 1 2 + 4 * + 3 -'))
# Test.assert_equals(calc(""), 0, "Should work with empty string")
# Test.assert_equals(calc("1 2 3"), 3, "Should parse numbers")
# Test.assert_equals(calc("1 2 3.5"), 3.5, "Should parse float numbers")
# Test.assert_equals(calc("1 3 +"), 4, "Should support addition")
# Test.assert_equals(calc("1 3 *"), 3, "Should support multiplication")
# Test.assert_equals(calc("1 3 -"), -2, "Should support subtraction")
# Test.assert_equals(calc("4 2 /"), 2, "Should support division")
