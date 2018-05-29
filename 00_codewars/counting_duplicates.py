# https://www.codewars.com/kata/counting-duplicates/train

def duplicate_count(text):
  m = {}
  for x in text.lower():
    m[x] = m.get(x) + 1 if m.get(x) is not None else 1
  return len(list(filter(lambda x:x>1, m.values())))

# test.assert_equals(duplicate_count("abcde"), 0)
# test.assert_equals(duplicate_count("abcdea"), 1)
# test.assert_equals(duplicate_count("indivisibility"), 1)


print(duplicate_count("indivisibility"))