import random

def number_guess():
    number = random.randint(1, 100)
    attempts = 0

    print("===== Number Guessing Game =====")
    print("I have selected a number between 1 and 100.")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess > number:
            print("Too High!")

        elif guess < number:
            print("Too Low!")

        else:
            print("Congratulations!")
            print("You guessed the number in", attempts, "attempt(s).")
            break

number_guess()