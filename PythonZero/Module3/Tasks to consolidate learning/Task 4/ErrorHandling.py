def processText(text):
    while not text.replace(" ", "") or not text[:5].isalpha() or len(text) <= 2:
        text = input("Invalid input, please enter again" + "\n")
    return text

def stringInput(inputStr):
    while not inputStr.isalpha():
        inputStr = input("Invalid input, please enter again" + "\n")
    return inputStr

def processName(name):
    while not name.replace(" ", "").isalpha() or len(name) < 4:
        name = input("Invalid input, please enter again" + "\n")
    return name

# Placeholder for creating another function for a variable case of string that is not text


# Functions using Try
def handleIntegerWithTry():
    while True:
        try:
            integer = int(input("Enter again:" + "\n"))
            break
        except ValueError:
            print("The input is still invalid" + "\n")
    return integer

def handleFloatWithTry():
    while True:
        try:
            floatNum = float(input("Enter again: " + "\n"))
            break
        except ValueError:
            print("The input is still invalid")
    return floatNum

def convertFloatWithTry(number):
    if number.replace('.', '', 1).isdigit():
        number = float(number)
    else:
        number = handleFloatWithTry()
    return number

def convertIntWithTry(number):
    if number.isdigit():
        number = int(number)
    else:
        number = handleIntegerWithTry()
    return number

# Functions without using Try

def handleIntegerInput(number):
    converted = False
    new_number = 0
    while not number.isdigit() or number < 0: # includes negative numbers
        number = input("Invalid input, please enter again:")
        if number.isdigit():
            new_number = int(number)
            converted = True
    if number.isdigit:
        new_number = int(number)
    return new_number

def handleFloat(number):
    converted = False
    new_number = 0
    while not number.replace('.', '', 1).isdigit() or number < 0: # includes negative numbers
        number = input("Invalid input, please enter again:")
        if number.replace('.', '', 1).isdigit():
            new_number = float(number)
            converted = True
    if number.replace('.', '', 1).isdigit():
        new_number = float(number)
    return new_number

#
#
#
#
