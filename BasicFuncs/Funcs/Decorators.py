import time


def func_decorator(func):
    def wrapper(*args, **kwargs):
        print("===start===")
        result = func(*args, **kwargs)
        print("====end====")
        return result

    return wrapper


def speed_test_dec(func):
    def test_speed(*args, **kwargs):
        st = time.time()
        func_res = func(*args, **kwargs)
        et = time.time()
        print(f"Время работы функции: {et - st} сек")
        return func_res

    return test_speed


def some_func(word):
    print(f"func word = {word}")
    return word + " is good"


@speed_test_dec
def nod_func(a, b):
    """Описание: функция вычисляет НОД"""
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


@speed_test_dec
def fast_nod_func(a, b):
    """Описание: функция вычисляет НОД (быстрый метод)"""
    if a < b: a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a


# ===================================================
some_func = func_decorator(some_func)
res = some_func("bear")
print(res)
# ===================================================
# nod_func = speed_test_dec(nod_func)
res = nod_func(2, 100000)
print(res)

# fast_nod_func = speed_test_dec(fast_nod_func)
res = fast_nod_func(2, 100000)
print(res)
