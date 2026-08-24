import random

print("===== DICE GAME =====")

input("Press Enter to roll...")

player = random.randint(1, 6)
computer = random.randint(1, 6)

print("Your number:", player)
print("Computer number:", computer)

if player > computer:
    print("🎉 You win!")
elif player < computer:
    print("Computer wins!")
else:
    print("It's a draw!")