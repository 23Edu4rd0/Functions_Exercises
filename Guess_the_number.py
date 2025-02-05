import random

SECRET_NUMBER = random.randint(0, 100)
ATTEMPTS = 0


print("Welcome to the Number Guessing Game:")
print("I'm thinking of a number between 1 and 100")


while True:
    DIFFICULTY = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if DIFFICULTY == "easy":
        ATTEMPTS = 10
        break
    elif DIFFICULTY == "hard":
        ATTEMPTS = 5
        break
    else:
        print("Invalid option, Please type 'easy' or 'hard'.")

while True:
    try:
        guess = int(input("Make a guess: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        ATTEMPTS -= 1
        continue

    if guess == SECRET_NUMBER:
        print("Congrats, you discovered the secret number!")
        break

    elif guess > SECRET_NUMBER:
        print("Too high\nGuess again")

    elif guess < SECRET_NUMBER:
        print("Too low\nGuess again")

    ATTEMPTS -= 1
    print(f"You have {ATTEMPTS} attempts remaining to guess the number.")

    if ATTEMPTS == 0:
        print(f"Game over! The correct number was {SECRET_NUMBER}")
        break




