# https://www.codewars.com/kata/valid-braces/train

def validBraces(string):
  stack = []
  for x in string:
    if len(stack) > 0:
      if x + stack[-1] in [')(', '][', '}{']:
        stack = stack[0:-1]
      else:
        stack.append(x)
    else:
      stack.append(x)
  return stack == []

print(validBraces( "[(])" ))

# test.expect(validBraces( "()" ), True);
# test.expect(not validBraces( "[(])" ), False);
