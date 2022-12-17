a=int(input("enter the coefficient of a:"))
b=int(input("enter the coefficient of b:"))
c=int(input("enter the coefficient of c:"))
d=(b**2)-4*a*c
if d>0:
    r1=-b+math.sqrt(d)/(2*a)
    r2=-b-math.sqrt(d)/(2*a)
    print("the roots are",r1,r2)
elif d==0:
    r1=-b/(2*a)
    r2=-b/(2*a)
    print("the roots are",r1,r2)
else:
    print("the roots are imaginary")
