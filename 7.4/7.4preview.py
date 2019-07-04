import math

# #e.g 3.1
# r=float(input("请输入圆的半径"))
# print("周长为"+str(2*math.pi*r))
# print("面积为"+str(r**2*math.pi))

# # e.g 3.4
# a=float(input("请输入x^2的系数"))
# b=float(input("请输入一次方的系数"))
# c=float(input("请输入常数项的系数"))
# delta=b**2-4*a*c
# if delta>0:
#     print("有两个实根")
# elif delta<0:
#     print("没有实根")
# else :
#     print("有两个相同的实根")

# e.g 3.5
# score = int(input("请输入您的成绩"))
# b = 0
# if score // 90:
#     b = 5
# elif score // 80:
#     b = 4
# elif score // 70:
#     b = 3
# elif score // 60:
#     b = 2
# else:
#     b = 1
# print(b)

# try

try:
    x = int(input("请输入一个整数"))
    y = int(input("请输入一个整数"))
    print("x/y", x / y)
except ValueError:
    print("请输入整数")
except ZeroDivisionError:
    print("除数不能为0")
