a=int(input("enter the number:"))
c=0
while(a>=10):
    if(a%3==0):
        c=c+1
        a=a//3
    else:
        break
print(c)