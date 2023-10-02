class Car:
    def __init__(self, color, licensePlate, model):
        self.color = color
        self.licensePlate = licensePlate
        self.model = model
        self.speed = 0

    def start(self):
        print("The car has started!")

    def accelerate(self):
        self.speed += 1
        print(self.speed)

    def brake(self):
        self.speed -= 1
        print(self.speed)

    def turnOff(self):
        print("The car has turned off!")

    def printData(self):
        print("Color:", self.color)
        print("License Plate:", self.licensePlate)
        print("Model:", self.model)


car1 = Car("Yellow", "f93-3495", "Fiat")
car2 = Car("Red", "X83-3480", "Gol")
car3 = Car("Green", "384-3480", "Uno")

car1.start()
car1.accelerate()
car1.accelerate()
car1.accelerate()
car1.accelerate()
car1.brake()
car1.brake()
car1.brake()
car1.brake()
car1.turnOff()

car1.printData()
print(" ")
car2.printData()
print(" ")
car3.printData()
print(" ")