a = int(input('请输入百分制成绩:'))
b = 0
if (a < 0 or a > 100):
    b = -1
elif (a >= 90):
    b = 5
elif (a >= 80):
    b = 4
elif (a >= 70):
    b = 3
elif (a >= 60):
    b = 2
else:
    b = 1
if (b == -1):
    print('输入错误')
else:
    print(b)
