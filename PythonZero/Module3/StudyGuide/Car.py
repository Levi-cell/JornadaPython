class Car:
    # Attribute Constructor
    def __init__(self, year, model, brand, color, plate, chassis):
        self.year = year
        self.model = model
        self.brand = brand
        self.color = color
        self.plate = plate
        self.chassis = chassis
        self.speed = 0
        self.passengers = 0

    # Additional Methods
    def addPassengers(self, quantity):
        if quantity <= 4:
            self.passengers += quantity
        else:
            print("Please do not transport more than 4 passengers.\n")

    def startEngine(self):
        print('The car started!\n')
        self.speed = 0

    def turnOffEngine(self):
        print('The car turned off!\n')
        self.speed = 0

    def accelerate(self):
        self.speed += 1
        print('Speed: ', self.speed, "\n")

    def brake(self):
        self.speed -= 1
        print('Speed: ', self.speed, "\n")

car1 = Car(2017, 'Palio', 'Fiat', 'Silver', 'OWX2121', '1CWZIZ389VT007299')

car2 = Car(2020, 'Edge', 'Ford', 'White', 'PNM1277', '9BWZZZ377VT004251')
print("----------Car-----------")
print(car1.plate, "\n")

car2.addPassengers(3)

car1.startEngine()
car1.accelerate()
car1.accelerate()
car1.accelerate()
car1.accelerate()
car1.accelerate()
car1.brake()
car1.brake()
car1.brake()
car1.brake()
car1.brake()
car1.turnOffEngine()
print(" ")


class Truck(Car):
    def __init__(self, year, model, brand, color, plate, chassis, axle, maxWeight, driver):
        super().__init__(year, model, brand, color, plate, chassis)
        self.axle = axle
        self.maxWeight = maxWeight
        self.driver = driver

    def startEngine(self):
        print('The truck started!\n')
        self.speed = 0

    def turnOffEngine(self):
        print('The truck turned off!\n')
        self.speed = 0

    def addPassengers(self, quantity):
        if self.passengers + quantity <= 2:
            self.passengers += quantity
        else:
            print("Please do not transport more than 2 passengers.\n")

    def changeDriver(self, driver):
        self.driver = driver

    def printData(self):
        print('Year: ', self.year, "\n")
        print('Model: ', self.model, "\n")
        print('Brand: ', self.brand, "\n")
        print('Color: ', self.color, "\n")
        print('Plate: ', self.plate, "\n")
        print('Chassis: ', self.chassis, "\n")
        print('Axle: ', self.axle, "\n")
        print('Max Weight: ', self.maxWeight, "\n")
        print('Driver: ', self.driver, "\n")

print("------------ Truck----------")
truck1 = Truck(2020, 'L-312', 'Mercedes-Benz', 'Yellow', 'JNM2287', '1BOZZZ300VT004778',
               'Single Axle with Single Tires', 6000, 'Milena')

print(truck1.chassis)

print(truck1.addPassengers(1))

truck1.printData()

truck1.startEngine()
truck1.turnOffEngine()