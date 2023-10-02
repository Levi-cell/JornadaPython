class Square:
    def __init__(self, side):
        self.side = side

    def changeSideValue(self):
        newSide = float(input("Enter the new side length of the square:"))
        self.side = newSide

    def getSideValue(self):
        print("The new side length of the square is:", self.side)

    def calculateArea(self):
        area = self.side ** 2
        print("The area of your square is:", area)


square = Square(2)
square.getSideValue()
square.changeSideValue()
square.getSideValue()
square.calculateArea()