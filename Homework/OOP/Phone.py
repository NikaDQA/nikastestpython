class Phone:
  
  def __init__(self, number):
#Поле для опису номера
      self.number = number
#Захищене поле для лічильника вхідних дзвінків
      self._incoming_calls = 0
    
#Метод, щоб задати номер телефону
  def set_number(self, number):
      self.number = number

#Метод, який поверне нам кількість прийнятих дзвінків
  def get_incoming_calls_count(self):
      return self._incoming_calls

#Метод прийняти дзвінок, який додає до лічильника одиницю
  def receive_call(self):
    self._incoming_calls += 1


#Створіть три різні об’єкти телефону. 
phone1 = Phone("111-111-111")
phone2 = Phone("222-222-222")
phone3 = Phone("333-333-333")

#Поміняйте всім початковий номер.
phone1.set_number("77777777777")
phone2.set_number("88888888888")
phone3.set_number("99999999999")

#Прийміть по кілька дзвінків на кожному (різна кількість)
phone1.receive_call()
phone1.receive_call()
phone1.receive_call()
phone2.receive_call()
phone2.receive_call()
phone3.receive_call()

# Створення списку з об'єктів телефонів
phones = [phone1, phone2, phone3]

#Напишіть функцію, яка приймає список з об’єктів телефонів, а повертає загальну кількість прийнятих дзвінків з усіх телефоні

def total_incoming_calls(phones):
  total_calls =0
  for phone in phones:
    total_calls += phone.get_incoming_calls_count()
  return total_calls
  
# Виведення загальної кількості прийнятих дзвінків з усіх телефонів
print(total_incoming_calls([phone1, phone2, phone3]))