# https://www.codewars.com/kata/first-variation-on-caesar-cipher/train/python

def shift_char(c, shift):
  a = ord(c)
  if c.isupper():
    a = ord('A') + ((ord(c) + shift - ord('A')) % 26)
  if c.islower():
    a = ord('a') + ((ord(c) + shift - ord('a')) % 26)
  return chr(a)


def moving_shift(s, shift):
  m, n = divmod(len(s), 5)
  if n > 0:
    m += 1
  
  # s2 = ''.join(map(lambda c: chr(ord(c) + shift) if c.isalpha() else c, s))
  l = []
  for i, c in enumerate(s):
    l.append(shift_char(c, i + shift))
  l = ''.join(l)
  l2 = ['', '', '', '', '']
  for i, c in enumerate(l):
    l2[i//m] += c
  return l2

def demoving_shift(s, shift):
  s = ''.join(s)
  l = []
  for i, c in enumerate(s):
    l.append(shift_char(c, - i - shift))
  return ''.join(l)

print(moving_shift("I should have known that you would have a perfect answer for me!!!", 1))
print(demoving_shift(["J vltasl rlhr ", "zdfog odxr ypw", " atasl rlhr p ", "gwkzzyq zntyhv", " lvz wp!!!"], 1))

# print(moving_shift("I should have known that you would have a perfect answer for me!!!", 1))
# test.assert_equals(
#     moving_shift("I should have known that you would have a perfect answer for me!!!", 1), 
#     ["J vltasl rlhr ", "zdfog odxr ypw", " atasl rlhr p ", "gwkzzyq zntyhv", " lvz wp!!!"])
