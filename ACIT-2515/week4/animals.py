class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        print("DEFAULT")
    
class Dog(Animal):
    def make_sound(self):
        print ("woof")

class Cat(Animal):
    def make_sound(self):
        print ("meow")

