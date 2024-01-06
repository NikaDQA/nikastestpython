amount = int(input("Enter the amount in $ which you would like to receive: ")) 

while amount > 0:
  if amount // 1000:
    number_of_banknots = amount // 1000 
    message = (f"{number_of_banknots} banknots of 1000$")
    print(message) 
    amount = amount - number_of_banknots * 1000 
    
  elif amount // 500:
    number_of_banknots = amount // 500
    message = (f"{number_of_banknots} banknots of 500$")
    print(message) 
    amount = amount - number_of_banknots * 500
    
  elif amount // 200:
    number_of_banknots = amount // 200
    message = (f"{number_of_banknots} banknots of 200$")
    print(message) 
    amount = amount - number_of_banknots * 200
    
  elif amount // 100:
    number_of_banknots = amount // 100
    message = (f"{number_of_banknots} banknots of 100$")
    print(message)
    amount = amount - number_of_banknots * 100
    
  elif amount // 50:
    number_of_banknots = amount // 50
    message = (f"{number_of_banknots} banknots of 50$")
    print(message)
    amount = amount - number_of_banknots * 50
    
  elif amount // 20:
    number_of_banknots = amount // 20
    message = (f"{number_of_banknots} banknots of 20$")
    print(message)
    amount = amount - number_of_banknots * 20
    
  elif amount // 10:
    number_of_banknots = amount // 10
    message = (f"{number_of_banknots} banknots of 10$")
    print(message) 
    amount = amount - number_of_banknots * 10
  else:
    break