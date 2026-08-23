import random

input("Press Enter to roll the dice...")

dice = random.randint(1, 6)

print("🎲 You rolled:", dice)

if dice == 6:
    print("Great roll!")
elif dice == 1:
    print("Better luck next time!")
else:
    print("Nice roll!")