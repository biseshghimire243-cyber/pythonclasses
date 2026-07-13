import random

def winner(user, computer):

    if user == computer:
        return "Tie"

    elif (user == "snake" and computer == "water") or \
         (user == "water" and computer == "gun") or \
         (user == "gun" and computer == "snake"):
        return "User"

    else:
        return "Computer"


choices = ["snake", "water", "gun"]

user_score = 0
computer_score = 0

while True:

    user = input("\nEnter snake, water, gun or quit: ").lower()

    if user == "quit":
        break

    if user not in choices:
        print("Invalid choice!")
        continue

    computer = random.choice(choices)

    print("Computer:", computer)

    result = winner(user, computer)

    if result == "Tie":
        print("Match Tie!")

    elif result == "User":
        print("You Win!")
        user_score += 1

    else:
        print("Computer Wins!")
        computer_score += 1

print("\nFinal Score")
print("You:", user_score)
print("Computer:", computer_score)