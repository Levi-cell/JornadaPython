def menu():
    dishesDict = {}
    while True:
        dishName = input("Enter the name of the dish or beverage:" + "\n")

        while not dishName.replace(" ", "") or not dishName[:5].isalpha() or len(dishName) <= 2:
            dishName = input("Enter the dish name again:" + "\n")

        while True:
            try:
                price = float(input("Enter the price of the dish or beverage: " + "\n"))
                break
            except ValueError:
                print("Invalid input." + "\n")

        dishesDict[dishName] = price

        print("Updated menu:", "\n")
        for dish, dishPrice in dishesDict.items():
            print(f"{dish} : $ {dishPrice}")
        print(" ")
        option = input("Do you want to add another dish? Type S for Yes or N for No:" + "\n")
        if option == "N":
            break

    return dishesDict
