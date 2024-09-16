from linecache import clearcache

print("итерируемая неупорядоченная коллекция уникальных элементов")
a = {"yes", 1, 2, 3, "yes", 1, 2, 3}
print(a)
b = {1, 1.3, "yes", (1, 3)}
print("содержит только неизменяемые типы данных")
x = set()
y = {}
print(type(x), type(y))
print(set([1,2,3,4,5]), set("yesyes"))
print(set(range(7)))
for p in b:
    print(p)

b.add(1)
b.add(5)
b.update("asd")
b.update([4, 3, 8])
b.discard(5)
b.remove(1)
b.pop() #с пустым множеством будет ошибка
print("discard - не вернет ошибку если нет элемента, remove - вернет")
print(b)
b.clear()