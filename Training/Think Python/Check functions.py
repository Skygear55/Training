def any_lowercase1(s):
    ''' checks if first letter in string is lowercase
    '''
    for c in s:
        if c.islower():
            return True
        else:
            return False
        
def any_lowercase2(s):
    ''' Always returns True unless string is empty, then it returns None
    '''
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    ''' Checks whether the last letter in the string 
    is a lowercase
    if yes = True
    if no = False
    '''
    for c in s:
        flag = c.islower()
    return flag


def any_lowercase4(s):
    ''' Checks if there are any 
    lowercase letters in the string 
    '''
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    ''' Checks if all the letters 
    in the string are lowercase
    '''
    for c in s:
        if not c.islower():
            return False
    return True

print(any_lowercase5('cdo'))