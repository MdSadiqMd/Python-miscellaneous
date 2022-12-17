s=str(input())
percent=int(input())
result=""
for i in s:
    val=int((percent/100)*len(i))
    s1,s2=i[:val],i[:val]
    result=s1+" "+s2+" "
    print(result)

