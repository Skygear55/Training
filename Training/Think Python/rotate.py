#my version
def rotate_letter(letter, n ):
    rotated_letter = chr(ord(letter) + n)
    return rotated_letter
    

         
def rotate_word1(word, n):
    index = 0
    while index < len(word):
         letter = word[index]
         print(rotate_letter(letter, n ))         
         index = index + 1
        
        
def rotate_word2(word, n):
    res = ''
    for letter in word:
        res += rotate_letter(letter, n)
    return res
print(rotate_word2('melon', -10))


#Allen.B.Downey's version
def rotate_letter1(letter, n):
    """Rotates a letter by n places.  Does not change other chars.

    letter: single-letter string
    n: int

    Returns: single-letter string
    """
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter

    c = ord(letter) - start
    i = (c + n) % 26 + start
    return chr(i)


def rotate_word(word, n):
    """Rotates a word by n places.

    word: string
    n: integer

    Returns: string
    """
    res = ''
    for letter in word:
        res += rotate_letter(letter, n)
    return res

