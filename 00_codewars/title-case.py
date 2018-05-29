# https://www.codewars.com/kata/title-case/train

def title_case(title, minor_words=''):
  minor_words = minor_words.lower().split(' ')
  title = title.split(' ')
  for i, word in enumerate(title):
    if i == 0 or word.lower() not in minor_words:
      title[i] = word.title()
    else:
      title[i] = word.lower()
  return ' '.join(title)

print(title_case(''))
print(title_case('a clash of KINGS', 'a an the of'))
print(title_case('THE WIND IN THE WILLOWS', 'The In'))
print(title_case('the quick brown fox'))
# Test.assert_equals(title_case(''), '')
# Test.assert_equals(title_case('a clash of KINGS', 'a an the of'), 'A Clash of Kings')
# Test.assert_equals(title_case('THE WIND IN THE WILLOWS', 'The In'), 'The Wind in the Willows')
# Test.assert_equals(title_case('the quick brown fox'), 'The Quick Brown Fox')
