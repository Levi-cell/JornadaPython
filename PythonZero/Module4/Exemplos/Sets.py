# Sets do not have order and allow unique elements

firstSet = {2, 4, 5, 8}

print(firstSet)

print(type(firstSet))

print(len(firstSet))

print(" ")
listNumbers = [1, 2, 5, 6, 6, 7, 8, 8]
print(listNumbers)
print(len(listNumbers))
print(set(listNumbers))  # Notice that it ignores duplicates
print(len(set(listNumbers)))  # The size decreased
print(" ")
emptySet = set()
emptyDictionary = {}
print(type(emptySet))
print(type(emptyDictionary))

firstSet.add(10)  # Adds the specified element
print(firstSet)

firstSet.pop()  # Removes the first element
print(firstSet)

firstSet.remove(4)  # Removes the element you specify
print(firstSet)

evens = [2, 4, 6, 8, 10]  # Even elements
multiplesOfFour = [4, 8, 12, 16]  # Elements multiples of 4

# Intersection

# With lists, you can do it this way:

for x in evens:
    for i in multiplesOfFour:
        if i == x:
            print(x)

# With sets, you can do it this way
evens = set(evens)  # Converts to a set
multiplesOfFour = set(multiplesOfFour)

print(type(evens))
print(type(multiplesOfFour))

# Elements that are in evens AND in multiplesOfFour
print(evens.intersection(multiplesOfFour))
print(evens & multiplesOfFour)

# Elements that are in evens OR in multiplesOfFour
print(evens.union(multiplesOfFour))
print(evens | multiplesOfFour)

# Elements that are only in evens, in evens AND NOT (not in) in multiplesOfFour
print(evens.difference(multiplesOfFour))
print(evens - multiplesOfFour)
