def isDigit():
    letters = []
    numbers = []
    A = ['A', 1, 'E', 5, 'T', 7, 'W', 8, 'G']
    modifiedA = []

    for x in A:
        if type(x) != int:
            letters.append(x)
        else:
            numbers.append(x)

    numbers.reverse()
    modifiedA = [letters + numbers]
    print("List with letters only:", letters, "\n")
    print("List with reversed numbers:", numbers, "\n")
    print("Modified list:", modifiedA)

isDigit()