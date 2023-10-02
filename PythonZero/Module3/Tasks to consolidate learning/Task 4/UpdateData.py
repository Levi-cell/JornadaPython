from ErrorHandling import *

def updateWeight(personList):

    name = input("Enter the person's name:")
    # name = processName(name)

    personFound = False
    position = 0
    while not personFound and position < len(personList):
        if personList[position].name.lower() == name.lower():
            personList[position].updateWeight()
            print(f"{personList[position].name}'s weight has been updated to {personList[position].weight} kg")
            personFound = True
        position += 1
    if not personFound:
        print("Person not found")
    return personList


def updateAge(personList):
    name = input("Enter the person's name:")
    # name = processName(name)

    personFound = False
    position = 0
    while not personFound and position < len(personList):
        if personList[position].name.lower() == name.lower():
            personList[position].age += 1
            print(f"{personList[position].name}'s age has been updated and now they are {personList[position].age} years old.")
            print(f"Their current height is {personList[position].height}.")
            personFound = True
        position += 1
    if not personFound:
        print("Person not found")
    return personList