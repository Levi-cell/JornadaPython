import ListMaker
def processList():

    new_list = ListMaker.createList()

    letters = []
    numbers = []

    for x in new_list:
        if isinstance(x, int):
            numbers.append(x)
        else:
            letters.append(x)

    numbers.reverse()
    modified_list = [letters + numbers]

    print("List with letters only:", letters, "\n")
    print("List with reversed numbers:", numbers, "\n")
    print("Modified list:", modified_list)


processList()




