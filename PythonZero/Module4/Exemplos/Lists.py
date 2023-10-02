myList = [1, 2.5, "data", [4, 8]]
# Data of various types and lists within lists, data is mutable

myTuple = (1, 2, 3, 2, (2, 3))
# Tuples within tuples and data is immutable, it's only possible to change the entire tuple

myDictionary = {
    "AI": 1,
    "ML": 2,
    "DL": [3, 4]
}
# Mutable, concept of key-value pairs

mySet = {1, 2, 3}
# Mutable, unordered, unique elements

nameList = ['Sergio', "Maria", "Pedro"]

print(type(nameList))

mixedTypeList = [1, 2, True, [4, 5, 6]]

print(type(mixedTypeList))

# Another way to create a list

integerList = list([1, 2, 3])

print(integerList)

print(len(integerList))

print(mixedTypeList[0])
print(mixedTypeList[3])

print(mixedTypeList[3][1])
# It retrieves the list inside the list indicated by [3] and the number within it at position [1], which is 5

print(nameList[0:2])
# It starts at position 0 and goes up to one position before position 2

print(nameList[:2])

print(nameList[1:3])

print(nameList[1:2])

print(nameList[-1])
# It accesses the last value of the list, consider it like a cycle, position 3 comes before 0
# Positive positions are like an increasing mirror of negative positions

print(nameList[-2])

# : means up to
# :: reverses the order of the list

print(nameList[::-1])

print(type(nameList[1]))

print((nameList[1][0]))  # It treats a string as a list of characters

print(nameList[1][3])

# Lists are mutable

nameList[0] = "Mariana"
print(nameList)

# Strings are immutable

x = "Data"
# x[0] = "d"  ## This will give an error, it's not possible

# List concatenation

nameList1 = ["Fabio", "Sabrina"]

allNamesList = nameList + nameList1

print(allNamesList)

# List functions

# Min() gives us the smallest element in the list

print(min(integerList))
print(max(integerList))
print(sum(integerList))
print(type(integerList))
print(len(integerList))
print(range(len(integerList)))
# print(len(range(integerList))) ## This would give an error
rangeList = list(range(0, 10, 1))
# It will create a list from 0 to 10, or with 10 positions, skipping 1 number at a time
print(rangeList)

rangeList1 = list(range(0, 10, 2))
print(rangeList1)

# Native functions

languages = ["Python", "SQL", "R"]

languages1 = languages + ["Java", "C++"]

print(languages1)

languages1.clear()
print(languages1)

languages.append("Java")
languages.append("C++")

print(languages)

languages.append(["Java", "C++"])  # Adds as a list within another list
print(languages)

languages.extend(["Java", "C++"])  # Adds multiple elements
print(languages)

languages.insert(1, "Scala")  # Adds an element at the specified position

print(languages)

languages.remove("C++")  # Removes the first occurrence of "C++"
print(languages)

languages.pop(len(languages) - 1)  # Removes the element from the last position

print(languages)

languages.pop(2)  # Removes the element at position 2
print(languages)

print(languages.count("Java"))
# Counts how many times "Java" appears in the list, equal elements with the value "Java", in this case it's 2

nameList.sort()  # Sorts the elements in alphabetical order if they are strings or numerical if they are numbers
print(nameList)

rangeList.sort()  # Sorts numerically
print(rangeList)

# Sort doesn't work if you have various types of values.