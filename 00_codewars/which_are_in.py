# https://www.codewars.com/kata/which-are-in/train

def in_array(array1, array2):
  s = set()
  for x in array1:
    for y in array2:
      if x in y:
        s.add(x)
  return sorted(list(s))


print(in_array(["live", "arp", "strong"], ["lively", "alive", "harp", "sharp", "armstrong"]))
# a1 = ["live", "arp", "strong"] 
# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
# r = ['arp', 'live', 'strong']
# test.assert_equals(in_array(a1, a2), r)
