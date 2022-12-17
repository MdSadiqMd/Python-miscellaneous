a=[(1,3),(2,4)]
b=[]
for i in a:
    for j in i:
        if type[j]==int:
            b.append(j)
    print(b)