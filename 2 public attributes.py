class person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
p=person(str(input("enter name:")),int(input("enter age:")))
print(p.name)
print(p.age)