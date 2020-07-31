def main():
    txt = input()
    wordc = {}
    for e in ",?.!,":
        txt = txt.replace(e, ",")
    L = txt.split(",")
    L.sort()
    while L[0].isdigit() or L[0] == " ":
        del L[0]
    for e in L:
        if e in wordc:
            wordc[e] += 1
        else:
            wordc[e] = 1
    words = list(wordc.keys())
    print(words)
    words.sort()
    print(words)
    L1 = []
    for e in words:
        if wordc[e] >= 2:
            L1.append(e)
    else:
        print(L1)


main()
