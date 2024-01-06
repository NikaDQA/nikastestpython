print("Enter a number:")
Number = str(input())
length = len(str(Number))
index = 0
degree = length
while (index < length):
  degree = degree - 1
  coefficient = str(10**degree)
  digit = str(Number[index])
  message = (f"{digit} * {coefficient}")
  print(message)
  index= index + 1
