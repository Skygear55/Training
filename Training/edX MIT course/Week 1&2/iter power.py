def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    
    for i in range(base, exp):
        base = base*base
    return base
        
        
        
print(iterPower(-3.53, 8))
