def menu():
    dishes_dict = {}
    while True:
        dish_name = input("Enter the name of the dish or beverage:" + "\n")

        while not dish_name.replace(" ", "") or not dish_name[:5].isalpha() or len(dish_name) <= 2:
            dish_name = input("Enter the dish name again:" + "\n")

        while True:
            try:
                price = float(input("Enter the price of the dish or beverage: " + "\n"))
                break
            except ValueError:
                print("Invalid input." + "\n")

        dishes_dict[dish_name] = price

        print("Updated menu:", "\n")
        for x in dishes_dict:
            print(f"{x} : $ {dishes_dict[dish_name]}")
        print(" ")
        option = input("Do you want to add more dishes? Type Y or N:" + "\n")
        if option == "N":
            break

    return dishes_dict
