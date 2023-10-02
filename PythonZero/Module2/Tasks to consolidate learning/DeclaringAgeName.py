people_registered = []
ages = []
genders = []
women = []
men = []
above_average = []
below_average = []

people_data = [
    {'name': people_registered,
     'age': ages,
     'gender': genders}
]

while True:
    name = input("Enter the person's name:\n")
    people_registered.append(name)

    age = int(input("Enter the age of %s:\n" % name))
    ages.append(age)

    gender = input("%s, is the person female or male? Enter 'Female' or 'Male':\n" % name)
    genders.append(gender)

    if gender == "Female":
        women.append(name)
    elif gender == "Male":
        men.append(name)

    option = input("Do you want to add someone else? Enter 'Yes' or 'No':\n")
    if option == "No":
        break

average_age = sum(ages) / len(ages)

while True:
    choice = int(input("""What would you like to do now? Enter the option you want:
             1 - View the list of registered people
             2 - Average age
             3 - List of women
             4 - List of men
             5 - List of people above the average age
             6 - List of people below the average age
             7 - Exit the program\n"""))

    if choice == 1:
        print("The list is:", people_registered)
        print("The number of people is:", len(people_registered))
        option1 = input("Do you want to check more information about these names? Enter 'Y' or 'N':\n")
        if option1 == "Y":
            print(people_data)

    elif choice == 2:
        print("The average age is:", average_age)

    elif choice == 3:
        print("The list of women is:", women)

    elif choice == 4:
        print("The list of men is:", men)

    elif choice == 5:
        for name, age in zip(people_registered, ages):
            if age > average_age:
                above_average.append(name)
        print("List of people above the average age:", above_average)

    elif choice == 6:
        for name, age in zip(people_registered, ages):
            if age < average_age:
                below_average.append(name)
        print("List of people below the average age:", below_average)

    elif choice == 7:
        break

    option = input("Do you want to do something else? Enter 'Yes' or 'No':\n")
    if option == "No":
        break