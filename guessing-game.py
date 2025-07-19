import random

# Begin game and get possible number range
print("Welcome to the Number Guessing Game!")
min = int(input("Enter the minimum value for the range of possible numbers: "))
max = int(input("Now the maximum: "))

# Initialize Variables
num = random.randint(min, max)
guess = None
guesses = 0

# Core game logic
while guess != num:
    guess = int(input("Enter your guess: "))

    # Check if the guess is too high, low, or correct
    if guess > num:
        print("Too high, try again.")
        guesses += 1
    elif guess < num:
        print("Too low, try again.")
        guesses += 1
    else:
        guesses += 1

        # Restart or end the game
        restart = input("You got it in " + str(guesses) + " guesses! Would you like to play again? (Y/N): ").lower()
        if restart == 'y':
            min = int(input("Enter the minimum value for the range of possible numbers: "))
            max = int(input("Now the maximum: "))
            num = random.randint(min, max)
            guess = None
        else:
            print("Thanks for playing! Goodbye!")
            break