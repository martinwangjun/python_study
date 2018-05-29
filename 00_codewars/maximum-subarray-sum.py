# https://www.codewars.com/kata/maximum-subarray-sum/train

def maxSequence(arr):
  maxSum = 0
  total = 0
  for x in range(len(arr)):
    for y in range(x, len(arr)):
      total = sum(arr[x:y + 1])
      if total > maxSum:
        maxSum = total
  return maxSum

# 人家的方案
# def maxSequence(arr):
#   maxSum,curr=0,0
#   for x in arr:
#     curr+=x
#     if curr<0:curr=0
#     if curr>maxSum:maxSum=curr
#   return maxSum

print(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(maxSequence([-2, 1, 3, 4, -1, 2, 1, -5, 4]))
print(maxSequence([-1, -2]))
print(maxSequence([]))

# test.describe("Tests")
# test.it('should work on an empty array')   
# test.assert_equals(maxSequence([]), 0)
# test.it('should work on the example')
# test.assert_equals(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

