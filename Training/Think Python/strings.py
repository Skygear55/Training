def print_backwards(s): 
    index = len(s) - 1
    while index != len(s) - (len(s) + 1) :
        letter = s[index]
        print(letter)
        index = index - 1
        
def ducklings():     
    prefixes = 'JKLMNP'
    suffix = 'ack'
    prefixes2 = 'OQ' 
    suffixes2 = 'uack'
    for letter in prefixes :
        print(letter + suffix)
    for letter in prefixes2 :
        print(letter + suffixes2)      

def find(word, letter, n):
    index = n
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1


def count(word, letter1, n  ):
    ''' Counts the letters in a string 
      bukva = letter
      Word and bukva are strings 
      It prints them one by one on separate lines
    '''   
    
    find(word, letter1, n)
    count = n
    for letter in word:
        if letter == letter1:
           count = n    
           print(count )
        
                       
    
def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    
    i = 0
    j = len(word2) - 1

    while j >= 0:
        print(i, j)
        if word1[i] != word2[j]:
            return False
        i = i+1
        j = j-1

    return True

    
print(is_reverse('snots', 'stons'))








