from math import *


def dis(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def main():
    x = [1, -1, 2, -2, 4]
    y = [2, 3, 1.5, 0, 2]
    dd = []
    for i in range(len(x)):
        dd.append([])
        for j in range(len(x)):
            v = dis(x[i], y[i], x[j], y[j])
            dd[i].append(v)

main()
