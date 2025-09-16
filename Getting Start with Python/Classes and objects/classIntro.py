class Person2:
    name = "Deepika"
    city = "Mumbai"
p1 = Person2()
print(p1.name)
p1.name = "Ankita"
# del p1
# del p1.name
p1.ansicy = "something"
print(p1.ansicy,p1.name,sep= "\n")
print("_"*50)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Welcome {self.name}, your age is {self.age}")
p7 = Person("Kaushendra", 20)
p2 = Person("Ankit", 20)
p3 = Person()