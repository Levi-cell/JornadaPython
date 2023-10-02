from FuelPump import *
from Treatments import *

print("Welcome to the FUEL PUMP station! To start the day, enter the information below:")

fuelName = input("Enter the fuel name:")
fuelName = validateName(fuelName)

literPrice = input("Enter the liter price of the fuel:")
literPrice = convertFloatWithTry(literPrice)

fuelQuantityInPump = input("Enter the quantity of liters in the pump:")
fuelQuantityInPump = convertFloatWithTry(fuelQuantityInPump)
print(" ")

fuelStation = FuelPump(fuelName, literPrice, fuelQuantityInPump)

print("Check the station's information:" + "\n")
fuelStation.showData()

fuelType = []
extractedLiters = []
collectedValuesList = []

continueMenu = input("Enter anything to proceed to the menu:" + "\n")

while True:

    menu = input("""What would you like to do?
    1 - Refuel a vehicle
    2 - Change liter price
    3 - Change fuel type
    4 - Add fuel
    5 - Show station data
    6 - Check Earnings
    7 - Check all refueling data
    8 - End workday""" + "\n")

    if menu == "1":
        choice = input("Enter 1 to refuel by Liter, or enter 2 to refuel by Value:" + "\n")

        if choice == "1":
            fuel, collectedAmount, fuelWithdrawn = fuelStation.refuelByLiter()
            fuelType.append(fuel)
            collectedValuesList.append(collectedAmount)
            extractedLiters.append(fuelWithdrawn)
            if fuel and collectedAmount and fuelWithdrawn == 0:
                fuelType.remove(fuel)
                collectedValuesList.remove(collectedAmount)
                extractedLiters.remove(fuelWithdrawn)
            interaction = input("After reviewing the information, enter anything to return to the menu:")

        elif choice == "2":
            fuel, collectedAmount, fuelWithdrawn = fuelStation.refuelByValue()
            fuelType.append(fuel)
            collectedValuesList.append(collectedAmount)
            extractedLiters.append(fuelWithdrawn)
            if fuel and collectedAmount and fuelWithdrawn == 0:
                fuelType.remove(fuel)
                collectedValuesList.remove(collectedAmount)
                extractedLiters.remove(fuelWithdrawn)
            interaction = input("After reviewing the information, enter anything to return to the menu:")

        else:
            continueMsg = input("Invalid option, enter anything to return to the menu: " + "\n")

    elif menu == "2":
        fuelStation.changeLiterPrice()
        interaction = input("After reviewing the information, enter anything to return to the menu:")

    elif menu == "3":
        fuelStation.changeFuelType()
        interaction = input("After reviewing the information, enter anything to return to the menu:")

    elif menu == "4":
        fuelStation.addFuel()
        interaction = input("After reviewing the information, enter anything to return to the menu:")

    elif menu == "5":
        fuelStation.showData()
        interaction = input("After reviewing the information, enter anything to return to the menu:")

    elif menu == "6":
        print(f"The earnings so far is $ {sum(collectedValuesList)}")
        interaction = input("After reviewing the information, enter anything to return to the menu:")

    elif menu == "7":
        if not extractedLiters:  # Check if there are no orders yet
            print("No orders registered...")
        else:
            print("Orders made:")
            for i in range(len(extractedLiters)):
                print(f"{i + 1}º order:")
                print(f"- Fuel type: {fuelType[i]}")
                print(f"- Extracted liters: {extractedLiters[i]}L")
                print(f"- Collected value: $ {collectedValuesList[i]}")
                print("--------")
        print("/////////////////////////")

    elif menu == "8":
        print(f"The day ends with $ {sum(collectedValuesList)} ")
        break