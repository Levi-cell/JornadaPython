def validateText(text):
    while not text.replace(" ", "") or not text[:5].isalpha() or len(text) <= 2:
        text = input("Invalid input, please enter again:\n")
    return text

def validateString(string):
    while not string.isalpha():
        string = input("Invalid input, please enter again:\n")
    return string

def validateName(name):
    while not name.replace(" ", "").isalpha() or len(name) < 4:
        name = input("Invalid input, please enter again:\n")
    return name

# Space reserved for creating another function for a string variable case that is not text


# Functions that use Try
def validateIntWithTry():
    while True:
        try:
            integer = int(input("Enter again:\n"))
            break
        except ValueError:
            print("Input is still invalid.\n")
    return integer

def validateFloatWithTry():
    while True:
        try:
            integer = float(input("Enter again:\n"))
            break
        except ValueError:
            print("Input is still invalid.")
    return integer

def convertFloatWithTry(number):
    if number.replace('.', '', 1).isdigit():
        number = int(number)
    else:
        number = validateFloatWithTry()
    return number

def convertIntWithTry(number):
    if number.isdigit():
        number = int(number)
    else:
        number = validateIntWithTry()
    return number

# Functions that do not use Try

def validateInteger(number):
    converted = False
    new_number = 0
    while not number.isdigit() or number < 0: # includes negatives
        number = input("Invalid input, enter again:")
        if number.isdigit():
            new_number = int(number)
            converted = True
    if number.isdigit:
        new_number = int(number)
    return new_number

def validateFloatNumber(number):
    converted = False
    new_number = 0
    while not number.replace('.', '', 1).isdigit() or number < 0: # includes negatives
        number = input("Invalid input, enter again:")
        if number.replace('.', '', 1).isdigit():
            new_number = float(number)
            converted = True
    if number.replace('.', '', 1).isdigit():
        new_number = float(number)
    return new_number