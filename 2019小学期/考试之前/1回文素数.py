n = int(input("请输入一个四位数"))
a = n // 1000
b = n // 100 % 10
c = n // 10 % 10
d = n % 10
m = d * 1000 + c * 100 + b * 10 + a
result = (n == m)
print(result)
