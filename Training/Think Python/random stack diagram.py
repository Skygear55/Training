def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod

def a(x, y):
    x = x + 1
    return x * y

def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    return square

x = 1
y = x + 1
print(c(x, y+3, x+y))


''' 
_main_ ---> x = 1
            y = x + 1
c ---> x = 1 
       y = 5
       z = 6
total ---> 1 + 2 + 6
b ---> z = total => 1 + 2 + 6 => 9
a ---> x = x + 1 => 10 => a = 10 * 12
prod ---> a(9, 10) => prod = 9*10 = > 90
b ---> prod = 90
c ---> square = 90**2
'''

