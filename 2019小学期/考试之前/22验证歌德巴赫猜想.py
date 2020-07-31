def pm():
    N=int(input())
    while N<3 or N%2==1:
        print("error")
        N = int(input())
    pme=set()
    for i in range(2,N+1):
        pme.add(i)
    for i in range(2,N+1):
        if i in pme:
            for k in range(2*i,N+1,i):
                if k in pme:
                    pme.remove(k)
    for e in pme:
        f=N-e
        if f>=e and f in pme:
            print(N,"=",e,"+",f)
pm()