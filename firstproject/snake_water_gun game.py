import random

# Function to decide the winner
def winner(user, computer):

    if user == computer:
        return "It's a Tie!"

    elif (user == "snake" and computer == "water") or \
         (user == "water" and computer == "gun") or \
         (user == "gun" and computer == "snake"):
        return "You Win!"

    else:
        return "Computer Wins!"


choices = ["snake", "water", "gun"]

computer = random.choice(choices)

user = input("Enter snake, water, or gun: ").lower()

if user not in choices:
    print("Invalid Choice!")

else:
    print("You chose:", user)
    print("Computer chose:", computer)
    print(winner(user, computer))