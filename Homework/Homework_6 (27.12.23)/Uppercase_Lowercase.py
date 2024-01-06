# string1 = ["HELLO MY FRIENDS (LOWERCASE)"]
# string2 = ["Hello my friends (uppercase)"]


# result1 = map(lambda x: x.lower(), string1)
# print(list(result1))

# result2 = map(lambda y: y.upper(), string2)
# print(list(result2))


string = ["HELLO MY FRIENDS (LOWERCASE)","Hello my friends (uppercase)"]

result1 = map(lambda x: x.lower(), string)
print(list(result1))

result2 = map(lambda y: y.upper(), string)
print(list(result2))