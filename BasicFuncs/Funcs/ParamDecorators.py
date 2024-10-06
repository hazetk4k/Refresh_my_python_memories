import math
from functools import wraps


def dx_dec(dx=0.001):  # ссылка на эту фунцию вернет результат func_dec
    def func_dec(func):  # резултат фанкт дек есть функция wrapper
        @wraps(func) #__такиепараметры__ определяются как у func
        def wrapper(x, *args, **kwargs):  # результат wrapper - искомый
            """ВЫЧИСЛЕНИЕ ПРОИЗВОДНОЙ ФУНКЦИИ FUNC"""
            res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
            return res

        # wrapper.__name__ = func.__name__    #такой метод позволит функции сохранить имя
        # wrapper.__doc__ = func.__doc__      #сохранение описания метода sin_dx
        return wrapper

    return func_dec


@dx_dec(dx=0.00001)
def sin_df(x):
    """ВЫЧИСЛЕНИЕ СИНУСА X"""
    return math.sin(x)


# ===== можно писать так без @декоратора =======
# f = dx_dec(dx=0.0001)
# sin_df = f(sin_df)
# ===== или используй =======
# sin_df = dx_dec(dx=0.0001)(sin_df) #итого мы передаем функции sin_df результат wrapper, который результат func_dec, который результат sx_dec

# ===== сам вызов =======
# print("У незадекорированной функции имя: ", sin_df.__name__)
df = sin_df(math.pi / 3)
print(df)
print("У задекорированной функции имя: ", sin_df.__name__)
print(sin_df.__doc__)
