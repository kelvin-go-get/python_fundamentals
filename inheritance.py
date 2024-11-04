#Parent class
class Animal:
    def speak(self):
        print("ANIMAL IA SPEAKING")

#child class
class Dog(Animal):
    def bark(self):
        print("Dog is barking")
a = Animal()
b = Dog()
b.bark()
b.speak()