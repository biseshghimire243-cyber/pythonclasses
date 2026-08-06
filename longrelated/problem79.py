questions = {
    "Capital of Nepal": "Kathmandu",
    "5 + 7": "12",
    "Python is developed by?": "Guido van Rossum",
    "HTML stands for?": "HyperText Markup Language",
    "2 * 8": "16"
}

score = 0

try:

    print("\n========== QUIZ ==========")

    for question, answer in questions.items():

        user = input(question + " : ")

        if user.lower() == answer.lower():
            score += 1
            print("Correct\n")

        else:
            print("Wrong")
            print("Correct Answer:", answer)

    print("\nFinal Score:", score)
    print("Percentage:", (score / len(questions)) * 100, "%")

except Exception as e:
    print(e)