a=((1,2,3),(2,4,6),(5,6,7))
k=int(input("enter the number"))
for i in a:
    c=0
    for j in i:
        if (j%k)!=0:
            c=1
            break
    if c==0:
        print(i,end="")