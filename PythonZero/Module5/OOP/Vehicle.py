class Vehicle:
    def __init__(self, numberWheels, color, brand):
        self.numberWheels = numberWheels
        self.color = color
        self.brand = brand
        self.speed = 0

    def turnOn(self):
        print("The vehicle is on! Vroom!")

    def turnOff(self):
        print("The vehicle is off!")

    def accelerate(self):
        self.speed += 10
        print("You accelerated! Your current speed is:", self.speed)

    def brake(self):
        self.speed -= 10
        print("You braked! Your current speed is:", self.speed)

class Motorcycle(Vehicle):
    def __init__(self, numberWheels, color, brand):
        super().__init__(numberWheels, color, brand)

    def accelerate(self):
        self.speed += 5
        print("You accelerated! Now your speed is", self.speed)

    def brake(self):
        self.speed -= 5
        print("You braked! Your current speed is:", self.speed)

    def wheelie(self):
        print("The motorcycle is riding on one wheel! Be careful!")


motorcycle1 = Motorcycle(2, 'Blue', 'BMW')
motorcycle1.turnOn()
motorcycle1.accelerate()
motorcycle1.accelerate()
motorcycle1.wheelie()
motorcycle1.brake()
motorcycle1.brake()
motorcycle1.turnOff()