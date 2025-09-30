# Create a class of 'pets' from a class 'Animals' and further create a class 'Dog', 'Cat' from 'pets'. Add a method of 'woof', 'meow to class 'Dog' and 'Cat'....

class Animal:
    def __init__(self, name):
        self.name = name

    def speak (self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says meow!")

d = Dog("Bruno")
c = Cat("Luna")
d.speak()
c.speak()