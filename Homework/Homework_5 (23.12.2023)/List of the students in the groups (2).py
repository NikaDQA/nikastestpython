from collections.abc import Set


Python =  {'Ivan Ivanov','Dima Gorohov',"Nika Denysenko"}
Java = {'Max Moxov','Dima Gorohov'}
FullStack = {'Alex Sidorov','Dima Gorohov'}
FrontEnd = {'Petr Petrov','Alex Alekseev', 'Ivan Ivanov'}


group1 = set(Python) & set(Java)
group2 = set(Java) & set(FullStack)
group3 = set(FullStack) & set(FrontEnd)
group4 = set(Python) & set(FrontEnd)
group = set(group1) | set(group2) | set(group3) | set(group4)
print(f'Students who study in two or more groups:\n {group}\n')

group5 = set(Python) | set(Java)
group6 = set(group5) - set(FrontEnd)
group7 = set(group6) - set(FullStack)
print(f'Students who do not study on the FrontEnd:\n {group6}\n')

group8 = set(Python) ^ set(Java)
print(f'Students who learn Python or Java:\n {group7}\n')