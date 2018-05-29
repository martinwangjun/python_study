# https://www.codewars.com/kata/multiples-of-3-or-5/train

def solution(number):
  sum = 0;
  for x in range(0, number, 3):
    sum += x
  for x in range(0, number, 5):
    sum += x
  for x in range(0, number, 15):
    sum -= x
  return sum

# test.describe("Multiples of 3 and 5")
# test.it("should handle basic cases")
# test.assert_equals(solution(10), 23)
