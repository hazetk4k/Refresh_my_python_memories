b = map(int, ['4', '1', '2', '3'])
# b = int(x) for x in ['4','1','2','3']
# по сути мап возвращает генератор
# a = list(b)
# print(a)
for x in b:
    print(x, end=" ")
print()
# =========================================================
# x = map(len, ["Minsk", "Gomel", "Mogilev", "Vitebsk", "Grodno", "Brest"])
x = map(str.upper, ["Minsk", "Gomel", "Mogilev", "Vitebsk", "Grodno",
                    "Brest"])  # передаем ссылку на функцию которая должна работать с объектом
print(list(x))


# =========================================================
def func1_lower(s):
    return s.lower()


z = map(func1_lower, ["Minsk", "Gomel", "Mogilev", "Vitebsk", "Grodno", "Brest"])
print(list(z))

# лучше использовать lambda
c = map(lambda s: s.lower(), ["Minsk", "Gomel", "Mogilev", "Vitebsk", "Grodno", "Brest"])
print(list(c))

# =========================================================
v = map(int, input().split())
print(list(v))