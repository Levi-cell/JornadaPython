from Treatments import *

class FuelPump:
    def __init__(self, fuelType, literPrice, fuelQuantity):
        self.fuelType = fuelType
        self.literPrice = literPrice
        self.fuelQuantity = fuelQuantity

    def refuelByValue(self):

        collectedAmount = input(f"Enter the amount of money for {self.fuelType}")
        collectedAmount = convertFloatWithTry(collectedAmount)

        fuelWithdrawn = (collectedAmount * 1) / self.literPrice
        if self.fuelQuantity == 0:
            print("The fuel pump is empty. Add more fuel." + "\n")

        else:
            stop = False
            while not stop:
                if fuelWithdrawn > self.fuelQuantity:
                    print("The requested amount exceeds the available quantity..." + "\n")
                    choice = input(
                        f"""Currently, the fuel quantity is {self.fuelQuantity}L.
Enter 1 to try again, or enter anything else to go back to the menu.
                         """ + "\n")
                    if choice == "1":
                        collectedAmount = input(f"Enter again the amount in money for {self.fuelType}")
                        collectedAmount = convertFloatWithTry(collectedAmount)

                        fuelWithdrawn = (collectedAmount * 1) / self.literPrice
                    else:
                        stop = True
                        break

                else:
                    self.fuelQuantity -= fuelWithdrawn
                    stop = True
                    print(f"{fuelWithdrawn}L of {self.fuelType} has been refueled for ${collectedAmount}")
                    print(f"There is still {self.fuelQuantity}L of {self.fuelType} left in the pump.")
                    return self.fuelType, collectedAmount, fuelWithdrawn
        return 0, 0, 0

    def refuelByLiter(self):
        liters = input(f"Enter in liters how much {self.fuelType} you want")
        liters = convertFloatWithTry(liters)

        amount = (liters * self.literPrice) / 1
        if self.fuelQuantity == 0:
            print("The fuel pump is empty. Add more fuel." + "\n")

        else:
            stop = False
            while not stop:
                if liters > self.fuelQuantity:
                    print("The requested amount exceeds the available quantity..." + "\n")
                    choice = input(
                        f"""Currently, the fuel quantity is {self.fuelQuantity}L.
Enter 1 to try again, or enter anything else to go back to the menu.
                              """ + "\n")
                    if choice == "1":
                        liters = input(f"Enter again in liters how much {self.fuelType} you want")
                        liters = convertFloatWithTry(liters)

                        amount = (liters * self.literPrice) / 1
                    else:
                        stop = True
                        break

                else:
                    self.fuelQuantity -= liters
                    stop = True
                    print(f"{liters}L of {self.fuelType} has been refueled for ${amount}")
                    print(f"There is still {self.fuelQuantity}L of {self.fuelType} left in the pump.")
                    return self.fuelType, amount, liters
        return 0, 0, 0

    def changeLiterPrice(self):
        newLiterPrice = input("Enter the new fuel liter price:")
        newLiterPrice = convertFloatWithTry(newLiterPrice)

        self.literPrice = newLiterPrice
        print(f"The new liter price for {self.fuelType} is ${self.literPrice}")
        return self.literPrice

    def changeFuelType(self):
        newFuelType = input("Enter the name of the new fuel type:")
        newFuelType = validateName(newFuelType)

        self.fuelType = newFuelType
        print(f"The new fuel type is {self.fuelType}")
        return self.fuelType

    def addFuel(self):
        quantityAdded = input("Enter how many liters of fuel you want to add:")
        quantityAdded = convertFloatWithTry(quantityAdded)

        self.fuelQuantity += quantityAdded
        print(f"{quantityAdded}L has been added. The quantity in the pump is now {self.fuelQuantity}L")
        return self.fuelQuantity

    def showData(self):
        print("The current fuel is:", self.fuelType)
        print("The liter price is $", self.literPrice)
        print(f"The available quantity is {self.fuelQuantity}L")