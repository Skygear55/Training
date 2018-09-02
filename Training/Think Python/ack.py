def ack(m, n):
    ''' Evaluates the Ackerman function
    if m > 3 or n > 8 infinite recursion will occur 
    '''
    if m < 0 or n < 0:
        print ('Only positive integers allowed')
        return None 
    elif not isinstance(m, int) or not isinstance(n, int):
        print('Only integers allowed')
        return None
    elif m == 0:
        return n+1
    elif m > 0 and n == 0:
         return ack(m-1, 1)
    else:
        return ack(m-1, ack(m, n-1))
        
     
def ackermann(m, n):
    """Computes the Ackermann function A(m, n)

    See http://en.wikipedia.org/wiki/Ackermann_function

    n, m: non-negative integers
    """
    if m == 0:
        return n+1
    if n == 0:
        return ackermann(m-1, 1)
    return ackermann(m-1, ackermann(m, n-1))


print(ackermann(3, 8))


print(ack(3, 8))