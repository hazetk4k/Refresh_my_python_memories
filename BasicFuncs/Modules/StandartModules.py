from math import ceil as cl, pi
import time as tm
import pprint

# docs.python.org/3/library/

def ceil(x):
    print("local func ceil")
    return x

pprint.pprint(locals())
a = ceil(1.8)
b = cl(2.7)
print(a, b)
print(pi)
