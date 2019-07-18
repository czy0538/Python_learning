s=input()
sum=0
for i in range (0,len(s),1):
    sum+=int(s[i])**int(len(s))
else:
    if str(sum)==s:
        print("yes")
    else:
        print("no")
