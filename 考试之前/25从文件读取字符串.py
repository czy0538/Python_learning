
try:
    with open("D:\\A personal date\\GitHub\\Python_learning\\考试之前\\24.txt", "r") as f:
        s1=f.read()
        print(s1)
        f.seek(0)
        for t in f:
            print(t)
except FileNotFoundError:
    print("error")