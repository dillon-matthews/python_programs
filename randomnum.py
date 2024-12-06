import random

randNumber = random.randint(50, 100)
guess = 0
nGuesses = 0

while guess != randNumber:
    guess = int(input("Guess the number (between 50 and 100): "))
    nGuesses += 1
    if guess > randNumber:
        print("Too high, try again.")
    elif guess < randNumber:
        print("Too low, try again.")

print("Congratulations! You've guessed the correct number.")
print("Number of guesses:", nGuesses)
