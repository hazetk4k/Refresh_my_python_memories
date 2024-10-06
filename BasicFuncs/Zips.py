a = [1, 2, 3, 4]
b = [5, 6, 7, 8, 9, 10]
c = "python"

z = zip(a, b, c)
for i1, i2, i3 in z:
    print(i1, i2, i3)

z1, z2, z3, z4 = zip(a, b, c)
y1, *y2 = zip(a, b, c)
print(z1, z2, z3, z4)
print(y1, y2)
x = zip(a, b, c)
lz = list(x)
t1, t2, t3 = zip(*lz)
print(t1, t2, t3, sep='\n')