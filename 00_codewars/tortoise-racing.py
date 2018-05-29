def race(v1, v2, g):
  timer =[-1, -1, -1]
  if v1 >= v2:
    return timer
  second = int(g / (v2 - v1) * 3600)
  timer[0] = second // 3600
  timer[1] = (second % 3600) // 60
  timer[2] = (second % 60)
  return timer

print(race(720, 850, 70))
# Test.assert_equals(race(720, 850, 70), [0, 32, 18])
# Test.assert_equals(race(80, 91, 37), [3, 21, 49])
# Test.assert_equals(race(80, 100, 40), [2, 0, 0])
