a=int(input("enter the number:"))
import math
sum=0
num=a
l=0
while(num>0):
    l=l+1
    num=int(num/10)
    num=a
    while(num>0):
        r=num%10
        sum=sum+math.pow(r,l)
        num=int(num/10)
if (sum==a):
    print("amstrong")
else:
    print("not amstrong")