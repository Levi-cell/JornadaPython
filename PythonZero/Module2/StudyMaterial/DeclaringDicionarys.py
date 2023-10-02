# Dictionaries are written with curly braces and support various data types,
# using the syntax

######### DECLARING DICTIONARIES
# Let's create an employee as an example

employee = {"EmployeeID": 123, "Name": "José", "age": 20, "salary": 9200.45}

empty = {}  # creating an empty dictionary

print("All keys of the employee: ", employee)
print("Only the EmployeeID key of the employee:", employee["EmployeeID"])
print(empty)

print(type(employee))