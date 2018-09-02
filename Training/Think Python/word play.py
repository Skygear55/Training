fin = open('words.txt')
line = fin.readline()
word = line.strip()    

def word_20():
    line = fin.readline()
    word = line.strip()
    for line in fin:
        if len(line) > 20 :
            print(line)

def has_no_eshit(word,forbidden): 
    line = fin.readline()
    for forbidden in word:
        if forbidden not in word :
          print(line)   
          return True
    return False

def has_no_e(word,forbidden):
    for letter in word:
        if letter == forbidden:
            return False
    return True



def avoids(forbidden):
    input('Input word plox !')
    word = input()    
    for letter in word:
        if letter in forbidden:
            return False
    return True

def avoids1():
    input('Input forbidden letters plox !')
    forbidden = input()    
    for letter in line:
        if letter not in forbidden:
            print(line)
    return True        
    


def uses_only(word, available):
    for letter in word: 
        if letter not in available:
            return False
    return True


def is_abecedarian(word):
    previous = word[0]
    for c in word:
        if c < previous:
            return False
        previous = c
    return True

print(is_abecedarian('adc'))
    