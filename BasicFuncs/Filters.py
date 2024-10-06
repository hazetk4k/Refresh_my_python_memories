def prostoe(x):
    d = x - 1
    if d < 0:
        return False
    while d > 1:
        if x % d == 0:
            return False
        d-=1
    return True


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = filter(lambda x: x % 2 == 0, a)
c = filter(prostoe, a)
print(tuple(b))
print(tuple(c))

