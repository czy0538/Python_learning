for i in range(1,10,1):
    a=""
    for j in range(1,i+1,1):
        a+=str(i)+"*"+str(j)+"="+str(i*j)+" "
    print(a)