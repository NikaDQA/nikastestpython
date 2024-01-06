with open ("main.py", "r") as NewFile:
  data=NewFile.readlines()
for i in range(len(data)):
  print (data[len(data)-1-i])