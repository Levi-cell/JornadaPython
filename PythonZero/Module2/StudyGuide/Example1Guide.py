nameList = []
gradeList = []
absenceList = []
suspensionList = []

while True:
    name = (input('Enter the student name: ' + "\n"))
    nameList.append(name)
    absences = (int(input("Enter the number of absences: " + "\n")))
    absenceList.append(absences)
    grade = (float(input("Enter the student's grade: " + "\n")))
    gradeList.append(grade)
    suspension = (input("Enter 'S' if the student has had any suspension, and 'N' if the student has never been suspended: " + "\n"))
    suspensionList.append(suspension)

    if grade >= 60 and absences <= 10 and suspension == "N":
        print("The student passed the year")
    else:
        print("The student did not pass the year")

    option = (input("Do you want to add another student? Type 'Y' for yes or 'N' for no:" + "\n"))
    if option == "N":
        totalGrades = 0
        numStudents = 0
        for x in range(len(nameList)):

            if gradeList[x] >= 60 and absenceList[x] <= 10 and suspensionList[x] == 'N':
                print("Student", nameList[x], "passed the year")
            else:
                print("Student", nameList[x], "did not pass the year")

            totalGrades += gradeList[x]
            numStudents += 1

        print("The average annual performance of the school is:", totalGrades / numStudents)
        break