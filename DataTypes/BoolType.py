print("Бул может быть True или False.\n"
      "Получить такие значения можно выполнив любую проверку "
      "с помощью разных операторов (сравнения например):")
a = 5
b = 7
x = a > b
print(f"a = {a}, b = {b}, x = a > b = {x}, где type(x) = {type(x)}")

print("\n======================================================================")
print("Операторы сравнения: >, <, ==, !=, >=, <=. C ними трудностей быть не должно :)")

print("\n======================================================================")
print("Для объединения условий используются операторы and и or:")
print("and -> оба выражения true -> результат =  true иначе false")
print("or -> хотя бы одно выражение true -> результат = true иначе false")

print("\n=========================_AND_============================")
y = 4
a = 2
b = 5
x = y >= a and y <= b # но вообще лучше писать так: x = a <= y <= b
print(f"y = {y}, x = y >= {a} and y <= {b} = {x}")

print("\n=========================_OR_=============================")
y = -3
a = 2
b = 5
x = y <= a or y >= b
print(f"y = {y}, x = y <= {a} or y >= {b} = {x}")

print("Поизменяй в коде 'y' и почувствуй разницу, если не понятно")

print("\n======================================================================")
print("Можно инвертировать бул, если подставить not перед выражением:")
a = 3
b = 4
print(f"(a>b) = { a > b } not(a>b) = { not(a > b) }")

print("\n======================================================================")
print("Приоритеты операторов 1 - or, 2 - and, 3 - not, то есть у not приоритет самый высокий.")
v = 6

o = (not(v % 2 == 0 and v % 3 == 0))
z = (not(v % 2 == 0 or v % 3 == 0))
n = (not v % 2 == 0 or v % 3 == 0)

print(f"Для примера приведу три почти одинаковых выражения, в которых просто изменю расположение скобок и опрератор:\n"
      f"v = {v}, тогда\n"
      f"(not(v % 2 == 0 and v % 3 == 0)) = {z}\n"
      f"(not(v % 2 == 0 or v % 3 == 0)) = {z}\n"
      f"(not v % 2 == 0 and v % 3 == 0) = {n}\n\n"
      f"В выражениях (v % 2 == 0) = {v % 2 == 0} и (v % 3 == 0) = {v % 3 == 0}\n")

print("\n===========================Выводы:=================================")
print(f"Пример не очень показательный, но все же в третьем случае явно видно,\n"
      f"что сначала выполится оператор not к выражению v % 2 == 0,\n"
      f"и лишь потом начнется проверка and.")