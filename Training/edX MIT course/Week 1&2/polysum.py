import math
def polysum(n, s):
    '''
    Input: n(number of sides) = int and s(lenght of each side) = int or float 
    Output: Sum of the area and square of the perimater of the regular polygon
    '''
    def p(n, s):
        '''
        Computes the perimeter for polysum
        '''
        return n*s
    def area(n, s):
        '''
        Computes the area of a regular polygon with sides n and lenght s
        '''
        return (0.25*n*s**2) / (math.tan(math.pi/n))
    
    polysum = area(n, s) + (p(n, s))**2
    return round(polysum, 4)

print(polysum(92, 89))