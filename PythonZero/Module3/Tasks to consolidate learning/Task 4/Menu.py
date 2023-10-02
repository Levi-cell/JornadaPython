from AddPerson import addPerson
from UpdateData import updateAge
from UpdateData import updateWeight

interactive = input("Welcome to the human manager, type anything to add a person: ")

person = addPerson()
personList = []
personList.append(person)

while True:
    print("What would you like to do now?")

    menu = input("""
    1 - Add another person
    2 - Update a person's age
    3 - Update a person's weight
    4 - Check information for all added persons
    5 - Exit the program
    Enter an option: """)

    if menu == "1":
        person = addPerson()
        personList.append(person)

    elif menu == "2":
        personList = updateAge(personList)

    elif menu == "3":
        personList = updateWeight(personList)

    elif menu == "4":
        i = 0  # variable just for counting people
        for x in personList:
            print(f" {i+1}º person: /name: {x.name} / age: {x.age} / weight: {x.weight} / height: {x.height}  ")
            i += 1

    elif menu == "5":
        break

    else:
        print("Invalid option")