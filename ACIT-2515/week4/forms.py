import math

class Shape:
    def __init__(self, sides):
        self.sides = sides
    
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(4)
        self.lenght = length
        self.widht = width

    def area(self):
        return self.lenght * self.width

class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

class Circle(Shape):
    def __init__(self, radius):
        super().__init__(0)
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

# s = Square(20)
# s.lenght(20)
# s.sides(4)
