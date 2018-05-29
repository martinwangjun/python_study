
def comp(a1, a2):
  if a1 == None or a2 == None:
    return False
  a1 = map(lambda x: x*x, a1)
  s1 = set(a1)
  s2 = set(a2)
  if s1 == s2:
    return True
  else:
    return False

a1 = [35, 51, 7, 59, 17, 45, 45]
a2 = [1225, 2601, 49, 3481, 289, 2025, 2026]

# a1 = [121, 144, 19, 161, 19, 144, 19, 11]
# a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]

print(comp(a1, a2))

# test.assert_equals(comp(a1, a2), True)
