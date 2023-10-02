# Making it easier, the goal is to have the user input
# anything and then print that string right-justified in a 70-character wide space

# Variable stores one value at a time
# Parameter can be a variable, dictionary, list, function - it's always local and volatile,
# it can vary according to usage outside of the "def" definition


def rightJustify(s):  # s is a parameter
    spacesLeft = 70 - len(s)
    s = ' ' * spacesLeft + s
    print(s)


userInput = input("Enter anything: " + "\n")
rightJustify(userInput)
