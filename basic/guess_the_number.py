''''This is the guess the number game.
    Select a random number between 1 and 20 and try to guess.
'''
import random

#Ask for a name
print('Hello. What is your name?')
name = input()

print('Well, '+ name +', I am thinking of a number between 1 and 20.')
#Select a random number between 1 and 20.
secretNumber = random.randint(1, 20)

#Loop for input the number.
for i in range(1, 7):
    print('Take a guess. ')
    # Exception in case the input is not a number.
    try:
        numberGuess = int(input())
        if numberGuess > secretNumber:
            print("Your guess is to high.")
        elif numberGuess < secretNumber:
            print("Your guess is to low.")
        else:
            # Guessed the secret number, and out the loop
            break
    except ValueError:
        print("The input must be a number.")
    

#Print the results
 
if numberGuess == secretNumber:
    print("Good job, "+ name +"! You guessed my number in "+ str(i)+" guesses!")
else:
    print("Nope. The number I was thinkig of was "+ str(secretNumber))