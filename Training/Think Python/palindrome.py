def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:1]



'''
print(first('karcho'), end='')
print (middle('karcho'), end='')
print(last('karcho'), end='')
'''

#def is_palindrome(string):
   # if first(string) == last(string) and last(string) == first(string) and middle1(string) == middle2(string):  
    ## else:
       # return False
    

def is_palindrome(word):
    """Returns True if word is a palindrome."""
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))


print(is_palindrome('allen'))
print(is_palindrome('bob'))
print(is_palindrome('otto'))
print(is_palindrome('redivider'))