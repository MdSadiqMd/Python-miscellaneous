class person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return self.name+" is "+str(self.age)+" years old "
p=person(str(input("enter name:")),int(input("enter age:")))
print(str(p))
