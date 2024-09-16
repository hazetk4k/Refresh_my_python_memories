dict1 = {"yes": 123, "no": 2342, "mb": 545, True: 32323, (1, 2, 3): 10}
print(dict1, "ключи - любые не изменяемые типы данных")
del dict1[True]
print(dict1)
print("yes" in dict1)