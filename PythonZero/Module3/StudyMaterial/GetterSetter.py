# Getters and Setters
class Test:
    def __init__(self, value):
        self.x = value

    '''Getter method to return the value of attribute x:'''

    def get_value(self):
        return self.x  # here using return

    '''Setter method to assign a new value to attribute x without needing to instantiate the class again'''

    def set_value(self, v):
        self.x = v  # here using assignment


test = Test(10)  # instantiate a new object

print('Value of variable x inside the object:', test.get_value())  # try printing without get_value

val = int(input('Enter a numeric value:'))  # global variable

test.set_value(val)  # setting the value of val to the test object

print('Value of the object after assignment:', test.get_value())