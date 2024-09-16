setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6, 7}
setC = {8, 9, 10}
res = setA & setB
print(res)
# setA &= setB
# print(setA)
print(setA & setC)
print(setA.intersection(setB))
# setA.intersection_update(setB)
# print(setA)
print(setA | setB)  # union()
print(setA - setB)
print(setB - setA)
print(setA ^ setB)

setX = {5, 6, 7, 8, 9}
setY = {9, 8, 7, 6, 5}
print(setX == setY, setX != setY, setX < setY, setY < setX)
setY = {9, 8, 7}
print(setX > setY)
setY.add(22)
print(setX > setY)