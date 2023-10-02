# Example 1
print('-' * 33)
print("Example 1")

# Representing coordinates
latitude = 12.2515
longitude = 25.9878

latitudeMentorama = 23.4567
longitudeMentorama = -3.4495

latitudeOxford = 34.3223
longitudeOxford = -2.3455

latitudeStanford = 32.3522
longitudeStanford = -2.6955

# A better representation of coordinates

coordinates = (latitude, longitude)
print('The coordinates are:', coordinates)
print(type(coordinates))

# Example 2
print('-' * 33)
print("Example 2")

tupleExample = ('a', 'b', 'c')
x, y, z = tupleExample
# Here we are unpacking this tuple
# The idea is to have a "key" that refers to the elements of the tuple
# x refers to 'a', y refers to 'b', and z refers to 'c'
# This way, it is not necessary to enclose the element in quotes in the print statement
# Only the reference value is needed

print(x, y, z)

# Remember that lists and tuples have different semantic functions from each other
# Lists generally work with order, while tuples generally work with structure