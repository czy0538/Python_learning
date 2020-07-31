from functools import *

it = [2, -4, 9, -5, 6, 13, -12, -3]
s = filter(lambda x: x > 0, it)
sum1 = reduce(lambda x, y: x + y, s)
print(sum1)
