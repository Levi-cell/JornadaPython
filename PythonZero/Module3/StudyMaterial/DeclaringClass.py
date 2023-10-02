class Person:  # Create class

    def __init__(self, name, age):  # Define parameters with self being mandatory, and name and age being optional
        self.name = name  # Constructor
        self.age = age    # Constructor

# The init method is used to indicate a private method

# Notice that above we created a class with its constructor and parameters
# Below, outside the class indentation, we can create an object of the same class
# You just need to "assign" a variable to the class and define the parameters

person1 = Person('Maria', '33')  # Create a person object 1

person2 = Person('José', '25')   # Create a person object 2

print(person1.name, person1.age)  # Print the value of the name and age
print(person2.name)               # Print only the name