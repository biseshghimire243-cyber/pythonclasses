import math


class Shape:

    def area(self):
        pass


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Triangle(Shape):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


rectangle = Rectangle(10, 5)
circle = Circle(7)
triangle = Triangle(10, 8)

print("Rectangle Area:", rectangle.area())
print("Circle Area:", circle.area())
print("Triangle Area:", triangle.area())