import math

print("Question 8 letter a:")
print("""Answer: The reserved keywords are def, if, else, return none""")
print("-------------------------------------------------")

print("Question 8 letter b:")
print("""Answer: 
if: It determines an action based on a condition.
else: It determines a counteraction for when the condition of the if statement is not satisfied.
def: It creates an object, a function called bhaskara that can be invoked.
return: It returns a value from a function when a specific condition is met.""")

print("-------------------------------------------------")
print("Question 8 letter c:")

def bhaskara(a, b, c):
    delta = b**2 - 4 * a * c
    if delta < 0:
        return None
    else:
        roots = []
        m1 = math.sqrt(delta)
        r1 = (-b + m1) / (2 * a)
        roots.append(r1)
        r2 = (-b - m1) / (2 * a)
        roots.append(r2)
        return roots

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

result = bhaskara(a, b, c)
if result is None:
    print("There are no real roots for the equation.")
else:
    print("The roots of the equation are:", result)