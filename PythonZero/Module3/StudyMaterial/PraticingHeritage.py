# Declaring the Parent Class

class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def printName(self):
        print(self.firstName, self.lastName)


# Using the Person class to create an object x, and then calling the printName() method

x = Person("John", "Doe")
x.printName()


# Declaring the Child Class

class Student(Person):
    pass

y = Student("Alice", "Johnson")
y.printName()