def spam(number):
  return number * 'bulochka'




def shortener(string):
  init_string = string.split( )
  short_string = []

  for word in init_string:
    if len(word) > 6:
      short_string.append(word[:6]+'*')
    else:
      short_string.append(word)

  return ' '.join(short_string)
print(shortener('Thisdasdasd is a test6666fhgfhfghfh'))



def compare_ends(words):
  count = 0
  for word in words:
    if len(word) >= 2 and word[0] == word[-1]:
      count += 1
  return count

words = ['abc', 'xyz', 'aba', '1221', 'aabb', 'aaabbb']
print(compare_ends(words))




def my_sum(list_of_numbers):
  sum = 0
  for number in list_of_numbers:
    sum += number
  return sum







