x = 25
epsilon = 0.01
step = 0.1
guess = 0.0
num_guess = 0 # added line to show number of guesses 
while abs(guess**2-x) >= epsilon:
    if guess <= x:
        guess += step
        num_guess +=1 # added line that increases the numberOfGuesses by 1
        print(num_guess,step,guess)# This line will print the number of guesses and step and the change in value
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))
   