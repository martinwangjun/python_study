# https://www.codewars.com/kata/snail/train

# tip: zip(*iterator_object)
def snail(array):
  sn = []
  while len(array) > 0:
    for x in array[0]:
      sn.append(x)
    array = array[1:]
    array = list(zip(*array))[::-1]
  return sn



array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
print(snail(array))