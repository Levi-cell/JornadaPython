def sayHello():
    print("Hello, everyone!")

sayHello()

hello = sayHello()

print(hello)  # doesn't store anything as it's a method

def squared(x):
    print("The value squared is", x**2)

squaredValue = squared(10)

print(squaredValue)