n = int(input())
k = (n % 3 == 0) + (n % 5 == 0) * 2 + (n % 7 == 0) * 4
if k == 7:
    print("all")
elif k == 6:
    print("5and7")
elif k == 5:
    print("3and7")
elif k == 4:
    print("7")
elif k == 3:
    print("3and5")
elif k == 2:
    print("5")
elif k == 1:
    print("3")
else:
    print("none")
