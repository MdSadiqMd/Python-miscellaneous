a=[[(0,1),(2,3)],[(4,5),(6,7)],[(8,9)]]
b=['a','b','c']
c=0
for i in range (len(a)):
    for j in range(len(b)):
        a[i][j]=a[i][j]+tuple(b[c])
    c=c+1
print(a)