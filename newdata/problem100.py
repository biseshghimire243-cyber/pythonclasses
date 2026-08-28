questions = {
    "What is the capital of Nepal? ": "kathmandu",
    "Which language is used for web styling? ": "css",
    "What is 10 + 20? ": "30",
    "Which language is known for data science? ": "python"
}

score = 0

print("===== PYTHON QUIZ =====")

for question, answer in questions.items():

    user_answer = input(question).lower()

    if user_answer == answer:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("\nQuiz Completed!")
print("Score:", score, "/", len(questions))