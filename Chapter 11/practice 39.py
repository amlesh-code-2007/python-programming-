# mini project: RPG system with inheritance and polymorphism........

class character:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def attack(self):
        print(f"{self.name} attacks with a basic strike.")

class warrior(character):
    def attack(self):
        print(f"{self.name} swings a sword with strength level {self.level}!")

class mage(character):
    def attack(self):
        print(f"{self.name} casts a fireball with power level {self.level}!")

c1 = warrior("Thor", 5)
c2 = mage("merlin", 7)

c1.attack()
c2.attack()