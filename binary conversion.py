a=int(input("enter the number"))
while(a<0):
    n=int(input("enter different number"))
if a==999 :
    quit()
c=0
sum=0
while(a!=0):
    rem=a%2
    sum=rem*(10**c)+sum
    a=a//2
    c=c+1
print("the binary number is",sum)

