import math

def hypotenuse(a, b):
    sqa = a**2
    sqb = b**2
    sqc = sqa + sqb
    c = math.sqrt(sqc)
    return c

def is_between(x, y, z):
    if x <= y <= z:
        return True
    else:
        return False

print(is_between(7, 6, 7))
