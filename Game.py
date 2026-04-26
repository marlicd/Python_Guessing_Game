# Python Program for Number Guessing Game with Difficulty Levels

# Import random library to generate a random number
import random

# Ask user to choose difficulty
print("Choose Difficulty Level")
print("1. Easy (10 attempts)")
print("2. Medium (7 attempts)")
print("3. Hard (5 attempts)")

choice = input("Enter choice (1/2/3): ")

# Set number of attempts based on the users choice
if choice == "1":
    Attempts = 10

elif choice == "2":
    Attempts = 7

elif choice == "3":
    Attempts = 5

else:
    print("Invalid choice, defaulting to Easy")
    Attempts = 10

# Generate random number between 1 and 100
Secret_number = random.randint(1, 100)

# Start the game loop
while Attempts > 0:

    # Ask user for a guess
    Guess = int(input("Guess a number between 1 and 100: "))

    # Check if guess is correct
    if Guess == Secret_number:
        print("Correct! You guessed the number.")
        break

    # If guess is too low 
    elif Guess < Secret_number:
        print("Too Low")

    # If guess is too high
    else:
        print("Too High")

    # Reduce the number attempts
    Attempts = Attempts - 1

    # Show remaining attempts
    print(f"Attempts left: {Attempts}")

# If user runs out of attempts end the game
if Attempts == 0:
    print(f"Game Over. The number was {Secret_number}")