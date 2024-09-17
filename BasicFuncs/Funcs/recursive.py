def recursive(value):
    if value == 0:
        return
    else:
        print(value)
        recursive(value - 1)


def factorial(n):
    if n <= 0:
        return 1
    else:
        return n * factorial(n - 1)


recursive(10)
print(factorial(6)) #1*2*3*4*5*6=720
