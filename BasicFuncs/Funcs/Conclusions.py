def say_name(name):
    def speaker():
        print(f"Hello, {name}")

    return speaker


# ===============================================================
def counter(start=0):
    def step():
        nonlocal start
        start += 1
        return start

    return step


#===============================================================
def strip_string(strip_that = " "):
    def do_strip(string):
        return string.strip(strip_that)
    return do_strip



# ===============================================================
f = say_name("Alex")
f2 = say_name("Sasha")
f()
f2()
# ===============================================================
c1 = counter(10)
c2 = counter()
print(c1())
print(c1())
print(c2())
# ===============================================================
strip1 = strip_string()
strip2 = strip_string(" :;,.!*/")
that_string = " *I want to break free!!,   "
print(strip1(that_string))
print(strip2(that_string))