print("Example:")
print("     ")
print("     ")
for num in range(1, 10, 2):
    print(num)

print("Example:")
print("     ")
print("     ")

for letter in "Python":
    print(letter)

print("Example:")
print("     ")
print("     ")

studentGradeDict = {
    "Maria": 7.5,
    "Joao": 9,
    "Pedro": 6,
    "Mariana": 10,
    "Paulo": 6.5
}

# print(studentGradeDict['Maria'])
print("How to print each key and value of a dictionary")
for student, grade in studentGradeDict.items():  # student is the key, grade is the value, .items references the keys and values
    print(student, ":", grade)

print("Example:")
print("     ")
print("     ")

failedStudents = {}
passedStudents = {}

for student, grade in studentGradeDict.items():
    if grade < 7:
        failedStudents.update({student: grade})
    else:
        passedStudents.update({student: grade})

print("The passed students were", passedStudents)
print("The failed students were", failedStudents)

print("Example:")
print("     ")
print("     ")

l1 = range(1, 50, 2)
l2 = range(1, 50, 1)

print(len(l1))
print(len(l2))

for i, j in zip(l1, l2):
    if i * j > 100:
        break
    else:
        print("i times j is:", i * j)

print("Here the loop has already stopped!")
print(f"The next i and j would be: {i}, {j}")

print("Example:")
print("     ")
print("     ")

l1 = range(1, 50, 1)
for i in l1:
    if i % 2 == 0:
        print("This number is even:", i)
    else:
        continue

# the continue statement makes any event that falls into the else block to be ignored and returns to the IF block
# unlike the break statement, which stops the code execution