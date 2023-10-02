# Unlike lists, tuples are immutable and do not need []
# Tuples can also grow freely

# DECLARING A TUPLE
# Example 1
print("-" * 35)
print("Example 1:")
tuple1 = 'apple', 12345, 'Hello, world!'
print(tuple1)

# Example 2
print("-" * 35)
print("Example 2:")
t = 12345, 54321, 'Hello!'
print(t[0])

# Tuples inside other tuples
# Example 3
print("-" * 35)
print("Example 3:")
t = 12345, 54321, 'Hello!'

u = t, (1, 2, 3, 4, 5)

print(u)