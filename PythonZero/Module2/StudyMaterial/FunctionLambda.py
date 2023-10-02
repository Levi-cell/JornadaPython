print("#Lambda function that takes a value and returns its double")
print("_"*35)

double = lambda x: x * 2
print(double(3))

# Lambda function that takes two parameters
print("Lambda function that takes two parameters")
print("_"*35)

# variable  #command #parameters  #process
increase = lambda a, b: (a * b / 100)

# usage
increase(100, 5)