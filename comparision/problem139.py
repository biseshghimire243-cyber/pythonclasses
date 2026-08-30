player1 = int(input("Enter Player 1 score: "))
player2 = int(input("Enter Player 2 score: "))

if player1 > player2:
    print("Player 1 wins!")

elif player2 > player1:
    print("Player 2 wins!")

else:
    print("The game is a draw!")