print("Enter a fizz_number:")
fizz = int(input())

print("Enter a buzz_number:")
buzz = int(input())

print("Enter a random_number:")
random = int(input())

for i in range(1, random + 1):
  if not i % fizz and not i % buzz:
    print("FB", end='')
  elif not i % fizz:
    print("F", end='')
  elif not i % buzz:
    print("B", end='')
  else:
    print(i, end='')
i += 1