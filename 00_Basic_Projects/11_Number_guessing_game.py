# Number Guessing program using python
import random

lower_limit = 1
upper_limit = 100
is_running = True

answer = random.randint(lower_limit ,upper_limit)
guesses = 0

print("--- Number Guessing Program ---")
print(f"Select a number between {lower_limit} and {upper_limit}")

while True:
    guess = input("Enter Your Guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess<lower_limit or guess>upper_limit:
            print(f"Please enter a guess between {lower_limit} and {upper_limit}.")
        elif guess < answer:
            print("Too low !! Try again")
        elif guess > answer:
            print("Too High !! Try again")
        else:
            print("CORRECT !!")
            print(f"You had taken {guesses} Guesses. ")
            break
    else:
        print("Entered Guess is InValid !")
        print(f"Select a number between {lower_limit} and {upper_limit}")


