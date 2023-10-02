# Example 1:
print("Example 1")
print("-" * 35)

def helloWorld():
    print("Hello, world")

helloWorld()
print(' ')

# Example 2:
print("Example 2")
print("-" * 35)

def helloWorld1():
    return 'Hello, world!'

result = helloWorld1()
print(result)
print(' ')

# Example 3:
print("Example 3")
print("-" * 35)

def helloWorldWithName():
    name = input("Enter your name:")
    print(f"Hello, world! {name}")

helloWorldWithName()
print(' ')

# Example 4:
print("Example 4")
print("-" * 35)

def helloWorldWithName1(name = ""):
    print(f"Hello, world! {name}")

name1 = input("Enter your name:")
helloWorldWithName1(name1)
print(' ')