import random

number = random.randint(1,9)
chances = 1
print("Number Guessing Game")
print("Guess a number (between 1 and 9): ")
guess = input("Enter your guess: ")
guessInt = int(guess)
while chances < 5 :
    
    if guessInt == number :
        print("Congratulations, you win!!")
        break

    if guessInt != number :
        
        chances = chances + 1
        if guessInt < number :
            
            print("Your guess was too low: Guess a number higher than " + guess)
            
        if guessInt > number :
            print("Your guess was too high: Guess a number lower than " + guess)

        guess = input("Enter your guess: ")
        guessInt = int(guess)
        

if chances >= 5 :
    print("You lose!!")



