# 180400501 曹志远 斐波那契数列作业
def fibonacci():
    a = b = 1
    yield (a)
    yield (b)
    while True:
        a, b = b, a + b
        yield (b)


def m(n):
    i = 0
    for num in fibonacci():
        i += 1
        if i > n:
            break
        file.write(str(num) + " ")


n = int(input("请输入想输入的斐波那契数列长度"))
file = open("fibonacci.bin", "wt")
m(n)
file.close()
