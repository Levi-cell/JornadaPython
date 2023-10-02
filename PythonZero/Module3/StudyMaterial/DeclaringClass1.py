class Person:

    def __init__(self, name, age):  # Constructor
        self.name = name
        self.age = age

    def setName(self, name):  # Method
        self.name = name  # Method body

    def setAge(self, age):
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age