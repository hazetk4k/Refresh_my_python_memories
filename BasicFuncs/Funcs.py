import time

print()  # вызов функции
f = print  # функция
f("yes")


# dont repeat yourself - функции помогают избежать повторений
def send_mail(a):
    b = 9
    result = False if a > b else True
    print("Mail")
    return result


# пример функции вычисления НОДа двух чисел:
def nod_func(a, b):
    """Описание: функция вычисляет НОД"""
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def fast_nod_func(a, b):
    """Описание: функция вычисляет НОД (быстрый метод)"""
    if a < b: a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a


def test_nod(func):
    # test1
    a, b = 28, 35
    res = func(a, b)
    if res != 7:
        print("test1 - Error")
    else:
        print("test1 - OK")

    # test2
    a, b = 100, 1
    res = func(a, b)
    if res != 1:
        print("test2 - Error")
    else:
        print("test2 - OK")

    # test3
    a, b = 2, 100000000
    st = time.time()
    res = func(a, b)
    et = time.time()
    dt = et - st
    if res == 2 and dt < 1:
        print("test3 - OK")
    else:
        print("test3 - Error")


help(nod_func)
test_nod(nod_func)
print("=========================================================")
test_nod(fast_nod_func)
