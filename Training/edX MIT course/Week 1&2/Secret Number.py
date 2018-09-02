quizz = 0
num = 91
low = 0
high = 100
guess = (high + low)//2
print('Please think of a number between 0 and 100!')
while True:
    print('Is your secret number ', int(guess), '?')
    quizz = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if quizz == 'c':
        break
    elif quizz == 'h':
        high = guess
    elif quizz == 'l':
        low = guess
    else:
        print('Sorry, I did not understand your input.')
    guess = (high + low)//2  
    
print('Game over. Your secret number was: ', int(guess))


