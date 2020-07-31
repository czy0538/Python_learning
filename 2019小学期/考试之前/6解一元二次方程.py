from math import *

a = float(input("a"))
b = float(input("b"))
c = float(input("c"))
if a == 0:
    if b == 0:
        print("不是方程")
    else:
        x = -c / b
else:
    beta = b ** 2 - 4 * a * c
    if beta >= 0:
        x1 = -b + sqrt(beta)
        x2 = -b - sqrt(beta)
        print("x1=%.2f" % x1, "x2=%.2f" % x2)
    else:
        data = sqrt(-beta)
        real = float("%10.3f" % (-b / (2 * a)))
        imag = float("%10.3f" % (beta / (2 * a)))
        print("x1=", complex(real, imag), "x2=", complex(real, -imag))
