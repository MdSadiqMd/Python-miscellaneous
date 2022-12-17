a=(1,2,3,4)
b={'a':1,'b':2,'c':3,'d':4}
c={}
for i,j in zip(a,b.items()):
    c[i]=dict([j])
print(c)