print("Numeric Variables Examples:" + "\n")

#### Example 1

example1Result = "Result of example 1: "

a = 3
b = 2

print(example1Result + "\n" +str(a+b))
print("//////////////////////////////"+"\n")

#### Example 2 (another way of the above)

example2Result = "Result of example 2:"

print(example2Result + "\n" + str(3+2))
print("//////////////////////////////"+"\n")

#### Example 3

example3Result = "Result of example 3:"

a = 5
b = 10

print(example3Result + "\n" +str(a+b) + " " + str(type(a)))
print("//////////////////////////////"+"\n")

#### Example 4

example4Result = "Result of example 4:"

pi = 3.14


print(example4Result + "\n" + str(pi) + " " + str(type(pi)))
print("//////////////////////////////"+"\n")

#### Example 5 Difference between using dot and comma in numbers

example5Result = "Result of example 5:"

pi = 3.14


print(example5Result + "\n" + str(pi) + " " + str(type(pi)))
print("//////////////////////////////"+"\n")


############################# String Variables Examples

print("String Variables Examples:" + "\n")


#### Example 1
example1Result = "Result of example 1:"

a = 'Mentorama'


print(example1Result + " " + a + str((type(a))))
print("//////////////////////////////"+"\n")

#### Example 2
example2Result = "Result of example 2:"

a = """Everything in life depends on how much you want to eat someone
you work to eat someone, you study," oh he is kind"
it's all to eat someone damn"""

print(example2Result + a)
print("//////////////////////////////"+"\n")

#### Example 3

example3Result = "Result of example 3:"

print(example3Result + 'Ha'*3)

#### Example 4

example4Result = "Result of example 4:"

name = 'Mentorama'
a = name[0]
b = name[0:6]

print(example4Result + name + " " + a  + " " + b)
print("//////////////////////////////"+"\n")

############################ Examples with Logical Variables

print("Examples with Logical Variables:" + "\n")

#### Example 1
example1Result = "Result of example 1:"

status = True

print(example1Result + " " + str(status) + " " + str(type(status)))
print("//////////////////////////////"+"\n")

# Input Examples
print("Input Examples")

#### Example 1

example1Result = "Result of example 1:"

x = input("Enter a number:")

print(example1Result + " " + x)

#### Example 2

courseName = input("Enter your course:")

print("You entered %s" % courseName)

# Concatenating String and INT Methods

# STR
x = 'My crypto portfolio amount in dollars is '
y = 5000
print(x + str(y))

#%%

x = 'My crypto portfolio amount in dollars is '
y = 5000
print("%s%s" % (x, y))

# str.format()

x = 'My crypto portfolio amount in dollars is '
y = 5000
print("{}{}".format(x, y))

# f-string

x = 'My crypto portfolio amount in dollars is '
y = 5000
print(f'{x}{y}')