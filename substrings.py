s=input()
sub1=str(input("enter string1:"))
sub2=str(input("enter string2:"))
if sub1 in s and sub2 in s:
    result=s[s.index[sub1]+len[sub1]+1:s.index[sub2]]
 print (result)

 else:

    print("strings have no substrings")