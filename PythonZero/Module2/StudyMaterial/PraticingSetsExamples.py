#Declaring two sets
mySet = {1, 2, 3, 4, 1} # Creating a set with {}
mySet2 = set([1, 2, 8, 9, 10]) # Creating a set with set([])

#Printing the sets and their types
print("Set 1:", mySet)
print(type(mySet))
print("-" * 35)
print("Set 2:", mySet2)
print(type(mySet2))
print("-" * 35)

#Mathematical operations on sets
#Union
unionSet = mySet | mySet2
print("Union:", unionSet)
print("-" * 35)

#Intersection
intersectionSet = mySet & mySet2
print("Intersection:", intersectionSet)
print("-" * 35)

#Adding elements
mySet.add(5)
print("Addition:", mySet)
print("-" * 35)

#Updating the set
mySet.update([3, 4, 5, 6])

#In the update, it doesn't accept duplicate elements, so 6 is the new addition
print("Update:", mySet)
print("-" * 35)

#Removing element
mySet.discard(2)
print("Removal:", mySet)
print("-" * 35)

