a1 = {x ** 2 for x in range(1, 5)}  # set
a2 = [x ** 2 for x in range(1, 5)]  # list
a3 = {x: x ** 2 for x in range(1, 5)}  # dict
print(a1, "\n", a2, "\n", a3)
d = [1, 2, "3", "4", -4, 3, 4]
a4 = {int(x) for x in d}
print(a4)
dict1 = {"yes": 1, "no": 2, "what": 3, "perhaps": 4}
a5 = {key.upper(): int(value) for key, value in dict1.items()}
print(a5)
a6 = {int(x) for x in d if int(x) > 0}
print(a6)
a7 = {int(value):key for key, value in dict1.items() if 2<=int(value) <= 5}
print(a7)