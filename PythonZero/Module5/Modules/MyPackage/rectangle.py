import math as m

def area_ret(b,h):
    return b*h

def perimeter(b,h):
    p = 2*b + 2*h
    return p

def diagonal_ret(b,h):
    #a**2 = b**2 + c**2 nós queremos encontrar a
    a = b**2 + h**2
    a = m.sqrt(a)
    return a