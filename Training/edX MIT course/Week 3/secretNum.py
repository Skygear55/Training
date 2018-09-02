def isMyNumber(x):
    secretnumber = - 15
    if x > secretnumber:
        return 1
    elif x < secretnumber:
        return -1
    else:
        return 0

def jumpAndBackpedal(isMyNumber, ):
    '''
    isMyNumber: Procedure that hides a secret number. 
     It takes as a parameter one number and returns:
     *  -1 if the number is less than the secret number
     *  0 if the number is equal to the secret number
     *  1 if the number is greater than the secret number
 
    returns: integer, the secret number
    ''' 
    
    
    guess = 0
    if isMyNumber(guess) == 0:
        return guess
    sign = isMyNumber(guess)
    while isMyNumber(guess) != 0:
        if isMyNumber(guess) == -1:
            guess += 1
        elif isMyNumber(guess) == 1:
            guess -= 1
    return guess

print(jumpAndBackpedal(isMyNumber))