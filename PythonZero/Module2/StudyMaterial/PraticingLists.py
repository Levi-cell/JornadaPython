#Example 1
print("-" * 35)
print("Example 1:")

myList = list() # or myList = []
print(myList)

#Example 2
print("-" * 35)
print("Example 2:")

myList = [3, 2, 10, 1, 0]

print(len(myList))
print(myList[0]) # Getting the element at position 0

print(myList[0:2]) # Taking a slice from position 0 to 1 (exclusive)

print(myList[:3]) # All items except the last 2

print(myList[3:]) # Only the last 2 items

print(myList[:-1]) # All items except the last one

print(myList[1:-1]) # All items except the first and last ones

print(myList[:]) # All elements

print(myList) # All elements

#Example 3
print("-" * 35)
print("Example 3:")

myList = ["a"]
myList.append('b')
myList.append('c')

print(myList)

#Example 4
print("-" * 35)
print("Example 4 based on the previous:")

myList.extend('a' 'b' 'c') # Note that there's no need for commas

print(myList)

#Example 5
print("-" * 35)
print("Example 5 based on the previous:")

del myList[1] # Deletes the element at the specified position
print(myList)

#Example 6
print("-" * 35)
print("Example 6 based on the previous:")

myList.insert(0, 'a')
print(myList)

# 'a' at position 0, regardless of any existing elements
#Other elements will shift to the right
#Example 7
print("-" * 35)
print("Example 7 based on the previous:")

myList.remove('a') # Removes the first occurrence of character 'a' from the list

#Raises an error if the item is not found in the list
print(myList)

#Example 8
print("-" * 35)
print("Example 8 based on the previous:")

myList.pop(2) # Removes an item at a specified position in the list and returns it
print(myList)

#Example 9
print("-" * 35)
print("Example 9 based on the previous:")

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple') # Counts how many times 'apple' appears

#I've translated the code into English and used camelCase for variable names.