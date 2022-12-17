a=int(input("enter number1:"))
b=int(input("enter number2:"))
if b>a:
    minimum=a
else:
    minimum=b
for i in range(1,minimum+1):
    if a%i==0 and b%i==0:
        GCD=i
print("the GCD is:",GCD)
