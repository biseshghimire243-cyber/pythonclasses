secret_number = 7

while True:
    guess = int(input("Guess the number: "))

    if guess == secret_number:
        print("Correct! You guessed it.")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")