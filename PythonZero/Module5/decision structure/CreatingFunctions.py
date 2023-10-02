def squaredFunction(x):
    return x**2

squaredValue = squaredFunction(10)

print(squaredValue)

def add(x, y):
    return x + y

sumResult = add(100, 75)
print(sumResult)

def identifyEven(x):
    if x % 2 == 0:
        print(x, "is even")

identifyEven(10)

def identifyEvenInList(lst):

    """\n
    Returns a list of even numbers from the input list"""

    evens = []
    for i in lst:
        if i % 2 == 0:
            evens.append(i)
        else:
            continue
    return evens

evenList = identifyEvenInList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(type(identifyEvenInList))

help(identifyEvenInList)
# Thanks to comments on line 23 within the function, using help on the created fu



