class Rectangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def changeValues(self):
        newBase = float(input("Enter the value of the base: "))
        newHeight = float(input("Enter the value of the height: "))
        self.base = newBase
        self.height = newHeight

    def returnSideValues(self):
        print(f"Your new base is: {self.base}")
        print(f"Your new height is: {self.height}" + "\n")
        return self.base, self.height

    def calculateAreaPerimeter(self):
        area = self.base * self.height
        perimeter = 2 * (self.base + self.height)
        print(f"The area of the room is {area}")
        print(f"The perimeter is {perimeter}" + "\n")
        return area, perimeter


room = Rectangle(base=0, height=0)
room.changeValues()
room.returnSideValues()

areaRoom, perimeterRoom = room.calculateAreaPerimeter()

baseboardLength = float(input("Enter the length of your baseboard: "))
baseboardHeight = float(input("Enter the height of your baseboard: "))

tileSide = float(input("Enter the side length of the tile: "))

quantityBaseboard = (perimeterRoom) / (baseboardLength * baseboardHeight)
quantityTile = (areaRoom) / (tileSide ** 2)

print(f"You will need {quantityTile} tiles for your room.")
print(f"You will need {quantityBaseboard} baseboards for your room.")