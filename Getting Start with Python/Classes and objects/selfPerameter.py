class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def displayInfo(self):
        print(f"Name: {self.name}, Age: {self.age}")

p1 = Person("Kaushendra", 20)
p1.displayInfo()
