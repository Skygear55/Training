def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    big = 0
    small = 0
    result = 0 
    if a > b:
        big = a 
        small = b
    else:
        small = a
        big = b
    if big - small == 0:
            return big
    if  a%(big - small) == 0 and b%(big - small) == 0 :
        result += (big-small)   
        return result   
    else:        
        return result + gcdRecur(small , big - small )
        



print (gcdRecur(753, 537))



elif aStr[len(aStr)//2] > char:
        aStr = aStr[0:len(aStr)//2]
    elif aStr[len(aStr)//2] < char:
        aStr = aStr[len(aStr)//2:]