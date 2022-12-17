dict={'a':1,'b':2,'c':3,'d':4}
print("dictionary in ascending order",*sorted (dict.items(),key=lambda x:x[1]))
print("dictionary in descending order",*sorted (dict.items(),key=lambda x:x[1],reverse=True))
