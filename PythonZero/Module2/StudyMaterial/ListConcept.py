############################## DECLARING LISTS
# Example 1:
print("-"*33)
print("Example 1:")

list0 = []  # Creating an empty list

print(list0)

# Example 2:
print("-"*33)
print("Example 2:")

list_x = [1, 2, 3]
print(list_x)  # with values

# Example 3:
print("-"*33)
print("Example 3:")
list_s = [1, "Hello world!", 1.1]
print(list_s)  # with values of different types

# IT'S POSSIBLE TO CREATE A LIST INSIDE ANOTHER LIST (nested lists)

# Example 4:
print("-"*33)
print("Example 4:")
list_d = ["Hello world", [1, 2, 3], "another_list", ["another_list"]]
# note:
# "Hello world" is at position 0 and is not a list, it's an element because it doesn't have []
# [1,2,3] is a list at position 1 of list_d
# "another_list" is not a list, it's an element because it doesn't have []
# ["another_list"] is a list because it has []

print(list_d[1])
print(list_d)

##################################################### LIST COMPREHENSION

# You can write shorter and more efficient code
# As a result, your code will be executed faster
# To create a list comprehension in Python, the syntax is as follows

# [expr for item in list]

# Example 5:
# Form without comprehension

print("-"*33)
print("Example 5:")
list_ = []
for item in range(10):
    list_.append(item ** 2)
print(list_)

# Example 6:
# With comprehension (applying the power of 2 to all items in the list)
print("-"*33)
print("Example 6:")

list1 = [item**2 for item in range(10)]  # The square of the index is the value at that index
print(list1)


######################## MULTIPLE List Comprehensions

# Example 7:
# Derived form
print("-"*33)
print("Example 7:")

transposed = []

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

# Creating a matrix
# 1,2,3,4 are in position 0 of the matrix
# 5,6,7,8 are in position 1 of the matrix

for i in range(len(matrix[0])):  # Range with the size of the matrix at position 0, looping through each position
    transposed_row = []

    for row in matrix:  # "row" is the position, it loops through each position of the matrix
        transposed_row.append(row[i])  # The value of that position goes to the transposed_row position
    transposed.append(transposed_row)

print("The original form:", matrix)
print("-"*33)
print("The transposed form:", transposed)

# Example 8:
# Simplified form
print("-"*33)
print("Example 8:")

transposeds = [[row[i] for row in matrix] for i in range(4)]
print("The original form:", matrix)
print("-"*33)

print("The transposed form:", transposeds)
print("-"*33)

print("For a more visible comparison, see the matrix before:")
print("-"*33)

for row in matrix:
    print(row)
print("-"*33)

print("For a more visible comparison, see the matrix now:")
for row in transposeds:
    print(row)