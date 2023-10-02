# Question 4

setX = set(["apple", "mango"])
setY = set(["mango", "orange"])
setZ = set(["mango"])

# a)
unionSet = setZ | setY.union(setX)

print("United we stand: ", unionSet, "\n")

# b)
intersectionXY = setX & setY

print("The intersection between X and Y is:", intersectionXY, "\n")

# c)
print("First way to check if it's a subset or not:",
      setX.issubset(setY | setZ), "\n")

print("Second way to check if it's a subset or not:",
      setX <= (setY | setZ), "\n")

print("Third way to check if it's a subset or not:",
      setX.issubset(setY.union(setZ)), "\n")

# d)
print("The elements that exist in X but not in Y are:", setX - setY, "\n")

# Extra question, proper subsets
print("Checking if X is a proper subset of the union of Y and Z:",
      setX < (setY.union(setZ)), "\n")

print("Checking if Z is a proper subset of Y:",
      setZ < setY, "\n")

print("Checking if Z is a subset of Y:",
      setZ <= setY, "\n")

print("Checking if Y is a subset of Z:",
      setY <= setZ, "\n")

print("Checking if Y is a proper subset of Z:",
      setY < setZ, "\n")