# https://www.codewars.com/kata/directions-reduction/train

def dirReduc(arr):
  stack = []
  for x in arr:
    if len(stack) > 0:
      if stack[-1] + x in ['EASTWEST', 'WESTEAST', 'SOUTHNORTH', 'NORTHSOUTH']:
        stack = stack[0:-1]
      else:
        stack.append(x)
    else:   
      stack.append(x)
  return stack
        
print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))


# a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
# test.assert_equals(dirReduc(a), ['WEST'])
# a = ["NORTH", "SOUTH", "SOUTH", "EAST", "NORTH", "WEST", "WEST"]
# test.assert_equals(dirReduc(a), ['SOUTH', 'EAST', 'NORTH', 'WEST', 'WEST'])
# u=["NORTH", "WEST", "SOUTH", "EAST"]
# test.assert_equals(dirReduc(u), ["NORTH", "WEST", "SOUTH", "EAST"])
