number_of_apartment = 40
number_of_floors = 5
number_of_apartments_per_floor= 4

total_apartments_in_entrance = number_of_floors * number_of_apartments_per_floor # 5*4=20
whole_part_of_entrances = number_of_apartment // total_apartments_in_entrance # 87 // 20 = 4.7
remainder_of_entrances = number_of_apartment % total_apartments_in_entrance # 87 % 20 = 7

entrance=0
if (remainder_of_entrances):
  entrance = whole_part_of_entrances + 1
  message = (f"Entrance {entrance}")
  print(message)
else:
  entrance = whole_part_of_entrances
  message = (f"Entrance {entrance}")
  print(message)

whole_part_of_floors = remainder_of_entrances // number_of_apartments_per_floor # 7 // 4 = 1
remainder_of_floors = remainder_of_entrances % number_of_apartments_per_floor # 7 % 4 = 3

normalized_numbers=number_of_apartment % total_apartments_in_entrance

if not normalized_numbers:
  message = (f"Floor {number_of_floors}")
  print(message)
  
if normalized_numbers:
  if remainder_of_floors:
    floor = whole_part_of_floors + 1
    message = (f"Floor {floor}")
    print(message)
  else:
    floor = whole_part_of_floors
    message = (f"Floor {floor}")
    print(message)
