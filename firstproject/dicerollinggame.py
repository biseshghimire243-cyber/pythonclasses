import random

def dice_game():

    while True:

        input("Press Enter to Roll the Dice...")

        dice = random.randint(1, 6)

        print("You rolled:", dice)

        again = input("Roll Again? (y/n): ")

        if again.lower() != "y":
            break

dice_game()