import math

# # 程序1 计算圆形面积
# r = float(input("请输入半径"))
# area = math.pi * pow(r, 2)
# print("面积为" + str(area))
#
# # 程序2 计算直角三角形面积
# a = int(input())
# b = int(input())
# print(a * b / 2)

# # 打印贺卡
# name = input("请输入发送人名字")
# to = input("请输入接收人名字")
# print("#################")
# print(to)
# print("       Merry Christmas to you")
# print("                yours" + name)
# print("#################")

# ## 求直角三角形斜边
# a = float(input("请输入边长"))
# b = float(input("请输入边长"))
# print(str((a**2+b**2)**0.5))

# # 小偷问题
# x = 1
# for x in range(1, 4):
#     if ((x != 1) + (x == 3) + (x == 4) + (x != 4) == 3):
#         print(chr(64 + x))

# 机智的输入
a = input()
b = input()
c = input()
print(eval(a + c + b))
