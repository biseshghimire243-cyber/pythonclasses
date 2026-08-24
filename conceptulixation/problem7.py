score = 0

print("===== SIMPLE QUIZ =====")

answer = input("What is the capital of Nepal? ")

if answer.lower() == "kathmandu":
    score += 1
    print("Correct!")
else:
    print("Wrong!")

answer = input("How many days are there in a week? ")

if answer == "7":
    score += 1
    print("Correct!")
else:
    print("Wrong!")

print("Your score:", score, "/ 2")