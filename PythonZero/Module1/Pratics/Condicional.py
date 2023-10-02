x = 0
y = 10

if x < y:
    print('yes')

if y < x:
    print('yes')  # not executed

if y == x:
    print('they are equal')  # not executed

print('they are not equal')  # executed because of the above if condition

if y ** 2 > x:
    print('yes')

if x:
    print('yes')  # anything that evaluates to 0 is considered false

if y:
    print('yes')

if x or y:
    print('yes')

if x and y:
    print("yes")  # not executable

if 'anç' in 'lembrança':
    print('yes')

if 'Paulo' in ['Paulo', 'Larissa', 'Diana']:
    print('yes')

# USING ELSE

if x > y:
    print("x is greater than y")
else:
    print("x is less than or equal to y")

# NESTED STRUCTURES

name = 'tiago'
last_name = 'Moreira'
last_last_name = 'Assunção'
if name == 'Felipe':
    print("Felipe")
    if last_name == 'Moreira':
        print("Moreira")
        if last_last_name == "Assunção":
            print("Assunção")
        else:
            print('Your last name is not Assunção')
    else:
        print("Your last name is not Moreira")
else:
    print("Your name is not Felipe")

# USING ELIF

course = 'Letras'
if course == "Fisica":
    print('My course is Physics')
elif course == 'Quimica':
    print("My course is Chemistry")
elif course == 'Informática':
    print("My course is Computer Science")
elif course == 'Matemática':
    print('My course is Mathematics')
else:
    print("The university does not offer this course! :/")

a = 25
b = 25

if b > a:
    print("b is greater than a ")
elif a == b:
    print("a and b are equal")