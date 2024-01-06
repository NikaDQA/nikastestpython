number = int(input("Enter a number: ")) 

if  number%2 and number>0:
  print("Be ready to see the diamond")
  for i in range(1,number+1):
    if i%2:
      a = (number - i)//2
      print(a*" ",i*"*",a*" ")
    i = i + 1

  for i in range(number-1,0,-1):
    if i%2:
      a = (number - i)//2
      print(a*" ",i*"*",a*" ")
    i = i - 1
else:
  print("Please input positive odd number")