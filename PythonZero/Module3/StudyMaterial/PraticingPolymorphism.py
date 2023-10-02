# Creating the parent class GeometricShape

class GeometricShape:
    def calcArea(self):
        pass


# Creating child classes derived from the parent class, subclasses:
#
# Square

class Square(GeometricShape):
    def __init__(self, side):
        self.side = side

    def calcArea(self):
        return self.side * self.side


# Circle

class Circle(GeometricShape):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return self.radius * self.radius * 3.14


# Using polymorphism

square1 = Square(2)
square2 = Square(3)
circle1 = Circle(1)
circle2 = Circle(2)

geometricShapes = [square1, square2, circle1, circle2]

totalArea = 0
for shape in geometricShapes:
    totalArea += shape.calcArea()

print(f"The total area is {totalArea}")
# or
# print(f"The total area is {format(totalArea)}")
# or
# print("The total area is {}".format(totalArea))