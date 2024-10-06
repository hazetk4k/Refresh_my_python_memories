import MyModules
import pprint
import sys

print(MyModules.floor(-5.4))
pprint.pprint(dir(MyModules))
a = MyModules.math.floor(5.6)
print(a)
pprint.pprint(sys.path)
