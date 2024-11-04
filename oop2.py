class Person:
    def __init__(self, name,age,gender,height):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height

    def movement(self):
        print("Person is walking")

a = Person("JOE" , 45,"mALE", 35)
print(a.name)
b = Person("Mary", 60, "Female", 160)
print(b.name)
c = Person("John", 50,"Male",150)
print(c.name)