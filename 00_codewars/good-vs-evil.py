# https://www.codewars.com/kata/good-vs-evil/train

good_worth = [1,2,3,3,4,10]
evil_worth = [1,2,2,2,3,5,10]

def goodVsEvil(good, evil):
  good = good.split(' ')
  evil = evil.split(' ')
  good = list(map(int, good))
  evil = list(map(int, evil))
  g = 0
  e = 0
  for i in range(0, len(evil)):
    e += evil[i] * evil_worth[i]
  for i in range(0, len(good)):
    g += good[i] * good_worth[i]
  # if (g < e):
  #   return 'Battle Result: Evil eradicates all trace of Good'
  # elif g > e:
  #   return 'Battle Result: Good triumphs over Evil'
  # else:
  #   return 'Battle Result: No victor on this battle field'
  return list(map(lambda x, y: x * y, good, good_worth))

x = [1, 2]
y = [1, 2]
print(x == y)   # True，比较值
print(x is y)   # False，比较的是否同一对象
y = x
print(x is y)

print(goodVsEvil('1 1 1 1 1 1', '1 1 1 1 1 1 1'))
# Test.assert_equals(goodVsEvil('1 1 1 1 1 1', '1 1 1 1 1 1 1'),  'Battle Result: Evil eradicates all trace of Good', 'Evil should win')
# Test.assert_equals(goodVsEvil('0 0 0 0 0 10', '0 1 1 1 1 0 0'), 'Battle Result: Good triumphs over Evil', 'Good should win')
# Test.assert_equals(goodVsEvil('1 0 0 0 0 0', '1 0 0 0 0 0 0'),  'Battle Result: No victor on this battle field', 'Should be a tie')

