list1 = ["x", "y", "z"]
list2 = [1, 2, 3]
a = dict.fromkeys(list1, list2)
print(a)
d = a.copy()
a.clear()
print(d)
d = {"yes":123, "no":58}
print(d["yes"])
print(d.get("uuuaaa", False))

print(d.setdefault("yes"),d.setdefault(3123), d.setdefault(0, 0))
print(d)

print(d.pop(0), d)
print(d.keys())
print(d.values())

for x in d:
    print(x)

for i in d.values():
    print(i)

for z in d.items():
    print(z)

for x, y in d.items():
    print(x, y)

d1 = {1:1, 2:2, 3:3}
d2 = {4:4, 5:5, 3:8}
d1.update(d2)
print(d1)
print(d1.get(4, False))
print(d1.setdefault(1))
print(d1.setdefault(10))
print(d1.setdefault(7, False))
print(d1)