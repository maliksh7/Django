# inheritence

class Animal():
    def __init__(self):
        print("Animal Created!")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")

class Dog(Animal):

    def __init__(self):
        # Animal.__init__(self)
        print("Dog Created!")

    def name(self):
        print("Rusty")

    def bark(self):
        print("WOOF")

    def color(self):
        print("Black")

mydog = Dog()
mydog.whoAmI()
mydog.eat()
mydog.bark()
mydog.color()
mydog.name()
