interaction = str(input("Let's check who passed the year or not, type any key to continue:" + "\n"))

nameList = []
annualAverageList = []
absenceList = []
suspensionList = []

while True:
    name = input('Enter the student name: ' + "\n")

    grade1 = float(input('Enter the grade for the first semester: ' + "\n"))
    while grade1 < 0 or grade1 > 10:
        print("You must have entered it wrong. Grades cannot be negative or greater than 10.")
        grade1 = float(input("Enter the grade again: " + "\n"))

    grade2 = float(input("Enter the grade for the second semester: " + "\n"))
    while grade2 < 0 or grade2 > 10:
        print("You must have entered it wrong. Grades cannot be negative or greater than 10.")
        grade2 = float(input("Enter the grade again: " + "\n"))

    grade3 = float(input("Enter the grade for the third semester: " + "\n"))
    while grade3 < 0 or grade3 > 10:
        print("You must have entered it wrong. Grades cannot be negative or greater than 10.")
        grade3 = float(input("Enter the grade again: " + "\n"))

    absences = int(input("Enter the number of absences: " + "\n"))
    suspension = input("Enter 'S' if the student has had any suspension, and 'N' if the student has never been suspended: " + "\n")

    annualAverage = (grade1 + grade2 + grade3) / 3

    nameList.append(name)
    absenceList.append(absences)
    suspensionList.append(suspension)
    annualAverageList.append(annualAverage)

    if annualAverage >= 6 and absences <= 10 and suspension == "N":
        print("%s has passed the year:" % name + "\n")
        print("The annual average was %f:" % annualAverage + "\n")
        print("The number of absences was %d:" % absences + "\n")
        print("And there were no suspensions" + "\n")
    else:
        print("%s did not pass the year" % name + "\n")
        print("The annual average was %f" % annualAverage + "\n")
        print("The number of absences was %d" % absences + "\n")
        print("And there was a suspension" + "\n")

    option = (input("Do you want to add another student? Type 'Y' for yes or 'N' for no:" + "\n"))
    if option == "N":
        while True:
            interactiveMenu = int(input("""What would you like to do next?
                1 - Access the names of failed students
                2 - Access the names of passed students
                3 - Calculate the average grade for the year
                Enter the option you want:""" + "\n"))

            if interactiveMenu == 1:
                for x in range(len(nameList)):
                    if annualAverageList[x] < 6 or absenceList[x] > 10 or suspensionList[x] != "N":
                        print("Student", nameList[x], "did not pass the year")

            elif interactiveMenu == 2:
                for x in range(len(nameList)):
                    if annualAverageList[x] >= 6 and absenceList[x] <= 10 and suspensionList[x] == "N":
                        print("Student", nameList[x], "passed the year")

            elif interactiveMenu == 3:
                print("The average performance of the students this year was: ", sum(annualAverageList) / len(annualAverageList))

            option = input("Do you want to do something else? Type 'Y' if yes or 'N' if no" + "\n")
            if option == "N":
                break