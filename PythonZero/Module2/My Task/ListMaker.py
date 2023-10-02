def createList():

    elementsList = []

    while True:

        choice = int(input(
            """What type of element do you want to insert? 
                1 - An integer
                2 - A letter""" + "\n"))

        if choice == 1:

            element = int(input("Enter a number between 0 and 9: " + "\n"))
            while element < 0 or element > 9:
                element = int(input("It must be a number between 0 and 9 and positive, enter again:" + "\n"))

            elementsList.append(element)

        if choice == 2:

            element = input("Enter an uppercase or lowercase letter:" + "\n")
            while not element.isalpha():
                element = input("Does not accept numbers. Enter an uppercase or lowercase letter:" + "\n")

            elementsList.append(element)

        option = input("Do you want to add more elements? Enter Y or N" + "\n")
        if option == "N":
            break

    print("Your original list is", elementsList)
    return elementsList
