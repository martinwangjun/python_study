# https://www.codewars.com/kata/format-a-string-of-names-like-bart-lisa-and-maggie/train

def namelist(names):
  return ' & '.join(map(lambda x: x.get('name'), names)).replace(' &', ',', len(names) - 2)

print(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]))
print(namelist([{'name': 'Bart'},{'name': 'Lisa'}]))
print(namelist([{'name': 'Bart'}]))
print(namelist([]))

# Test.assert_equals(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]), 'Bart, Lisa, Maggie, Homer & Marge',
# "Must work with many names")
# Test.assert_equals(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}]), 'Bart, Lisa & Maggie',
# "Must work with many names")
# Test.assert_equals(namelist([{'name': 'Bart'},{'name': 'Lisa'}]), 'Bart & Lisa', 
# "Must work with two names")
# Test.assert_equals(namelist([{'name': 'Bart'}]), 'Bart', "Wrong output for a single name")
# Test.assert_equals(namelist([]), '', "Must work with no names")
