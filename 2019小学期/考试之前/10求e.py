u,ev,i=1,1,1,
while(u>10e-6):
    u=u/i
    ev+=u
    i+=1
else:
    print(ev)