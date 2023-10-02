people_list = []
age_list = []

while True:
    name = input("What is the person's name:" + "\n")
    gender = input("What is %s's gender? Type 'Male' or 'Female':" % name + "\n")
    age = int(input("What is %s's age? " % name + "\n"))
    age_list.append(age)

    person_dict = {
        'Name': name,
        'Gender': gender,
        'Age': age
    }

    people_list.append(person_dict)  # Adding each person's dictionary to a list
    # Calculating the average age

    continuation = input("Do you want to add another person? Type 'Y' or 'N':" + "\n")

    if continuation == 'N':
        break

average_age = sum(age_list) / len(age_list)

while True:
    choice = int(input("""What would you like to do next? Enter the option you want:
                       1 - View the list of registered people
                       2 - Average age
                       3 - List of women
                       4 - List of men
                       5 - List of people above the average age
                       6 - List of people below the average age
                       7 - Exit the program""" + "\n"))

    if choice == 1:
        i = 0
        for person_dict in people_list:
            print("Information for person %d:" % (i + 1), person_dict, "\n")
            i += 1

    if choice == 2:
        print("The average age of people is", average_age)

    if choice == 3:
        print("Women on the list:", "\n")
        for person_dict in people_list:
            if person_dict['Gender'] == "Female":
                print(person_dict, "\n")

    if choice == 4:
        print("Men on the list:", "\n")
        for person_dict in people_list:
            if person_dict['Gender'] == "Male":
                print(person_dict, "\n")

    if choice == 5:
        print("People above the average age:")
        for x in people_list:
            if x['Age'] > average_age:
                print(x, "\n")

    if choice == 6:
        print("People below the average age:\n")
        for x in people_list:
            if x['Age'] < average_age:
                print(x, "\n")

    elif choice == 7:
        break

    option = input("Do you want to do anything else? Type 'Yes' or 'No':" + "\n")
    if option == "No":
        break