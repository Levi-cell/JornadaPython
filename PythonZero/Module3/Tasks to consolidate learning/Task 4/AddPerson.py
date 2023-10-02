from PersonClass import Person
from ErrorHandling import *


def addPerson():
    name = input("Enter the person's name:" + "\n")
    name = processName(name)

    age = input("Enter the person's age:" + "\n")
    age = convertIntWithTry(age)

    weight = input("Enter the person's weight in kg:" + "\n")
    weight = convertFloatWithTry(weight)

    height = input("Enter the person's height in cm:" + "\n")
    height = handleFloat(height)

    person = Person(name, age, weight, height)

    print(f"Congratulations, {person.name} has been successfully added.")

    return person