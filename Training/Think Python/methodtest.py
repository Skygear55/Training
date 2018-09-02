

def super_is_palindrome(string): 
    ''' If string  is palindrome it returns True
    If not , it returns None 
    '''
    if string == string[::-1] : 
        return True
 
print(super_is_palindrome('redivider'))