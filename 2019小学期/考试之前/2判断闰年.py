stry = input("请输入年份:", )
y = int(stry)
result = (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
print(result)
