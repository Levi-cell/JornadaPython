integerTuple = (1, 2, 3)

print(integerTuple)

print(type(integerTuple))

tuple1 = tuple((1, 2, 'a', True, "a"))  # We can create using the tuple method

print(tuple1)

print(type(tuple1))

print(len(integerTuple))
print(len(tuple1))

print(tuple1[2])

print(tuple1[-1])

tuple2 = tuple1 + integerTuple

print(tuple2)
print(tuple1 + integerTuple)

# integerTuple[0] = 2  # Error, tuples are immutable

print(tuple1.count('a'))  # There are two 'a' elements

print(tuple1.index('a'))  # It's at position 2