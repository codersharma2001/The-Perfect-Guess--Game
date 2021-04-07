import random
randNumber = random.randint(1,100)
userGuess = None
guesses=0

while userGuess != randNumber:
    userGuess=int(input("Enter the guess\n"))
    guesses += 1
    if (userGuess==randNumber):
        print("You guessed it right")

    else:
        if(userGuess>randNumber):
            print("You guessed it wrong ! Enter smaller number")

        else:
            print("You guessed it wrong ! Enter larger number")
    

print (f" You guesses {guesses} times")


















































