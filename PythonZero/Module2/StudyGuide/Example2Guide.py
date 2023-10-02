ageList = [11, 5, 18, 90]  # list
ageTuple = (11, 5, 18, 90)  # tuple

print('Values of the list:', ageList, "\n")
print('Values of the tuple:', ageTuple, "\n")

# The interpreter distinguishes between a list and a tuple by the symbols [] and ()

ageList[0] = 55
print("Updated values of the list:", ageList, "\n")

ageTuple[0] = 55  # An error message will appear on this line as tuples are not modifiable