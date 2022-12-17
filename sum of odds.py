sum=0
n=1
while(n<=100):
    if (n%2==0):
        sum=sum+n
        n=n+1
    else:
        n=n+1
        continue
print("the odd sum is",sum)
