from itertools import count

tuple1 = 1, 2
print(tuple1)
a = (1, 2, 3, 4, 5)
b = (1)
f = (1,)
print(b, f)
x, z = (1, 2)
print(x, z)
o, i = "ty"
print(o, i)
print(len(a), a[0], a[:4])
print("t = a[:] t ссылается на тот же кортеж, а не создается новый (копия)")
y = ()
z = tuple()
print(type(y))
print(type(z))
y = y + (1,)
print(y)
print(y*5)
print(a.count(1))
print(a.index(3))
print(a.count("hello"))
print(a.index(3, 2))

print("ЗНАТЬ!: ИНДЕКСЫ И СРЕЗЫ []; + * in; tuple(), len(), count(), index()")