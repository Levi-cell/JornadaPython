class A:
    a = 1  # Public attribute
    __b = 2  # Private attribute in class A


class B(A):  # Encapsulates A within B except for the private attributes of A

    __c = 3  # Private attribute in B

    def __init__(self):  # Constructor method
        print(self.a)
        print(self.__c)


a = A()

print(a.a)  # Prints 1

b = B()

# print(b.__b)  # Error, because __b is private to class A.

# print(b.__c)  # Error, __c is a private attribute, accessible only within the class.