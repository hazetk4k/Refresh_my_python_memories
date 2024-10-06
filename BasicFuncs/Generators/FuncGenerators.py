from string import ascii_lowercase, ascii_uppercase

chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"

def password_gen():
    pass

def get_sum(total):
    p = 0
    for z in range(total):
        z += 1
        p += z
        yield p


def balak_sequence(total):
    x1 = 0
    x2 = 0
    x3 = 0

    for i in range(total):
        if x1 == 0:
            x1 = 1
            yield 1
        elif x2 == 0:
            x2 = 1
            yield 1
        elif x3 == 0:
            x3 = 1
            yield 1
        else:
            x1, x2, x3 = x2, x3, x1 + x2 + x3
            yield x3


N = int(input())
x = get_sum(N)
for i in x:
    print(i, sep=" ")
n = balak_sequence(N)
for i in n:
    print(i, sep=" ")
