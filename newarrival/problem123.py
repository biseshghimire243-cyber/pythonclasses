questions = [
    {
        "question": "What is the capital of Nepal?",
        "options": ["A. Pokhara", "B. Kathmandu", "C. Dharan", "D. Lalitpur"],
        "answer": "B"
    },
    {
        "question": "Which language is used in this program?",
        "options": ["A. Java", "B. C++", "C. Python", "D. PHP"],
        "answer": "C"
    },
    {
        "question": "What keyword creates a function in Python?",
        "options": ["A. function", "B. def", "C. func", "D. create"],
        "answer": "B"
    },
    {
        "question": "Which data type stores key-value pairs?",
        "options": ["A. List", "B. Tuple", "C. Set", "D. Dictionary"],
        "answer": "D"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. <!-- -->", "C. #", "D. **"],
        "answer": "C"
    }
]


def start_quiz():

    score = 0

    print("\n========== PYTHON QUIZ ==========")

    for number, question in enumerate(questions, start=1):

        print("\nQuestion", number)
        print(question["question"])

        for option in question["options"]:
            print(option)

        answer = input("Your answer: ").upper()

        if answer == question["answer"]:

            print("Correct! ✓")
            score += 1

        else:

            print(
                "Wrong. Correct answer:",
                question["answer"]
            )

    percentage = (score / len(questions)) * 100

    print("\n========== RESULT ==========")
    print("Correct Answers:", score)
    print("Total Questions:", len(questions))
    print("Percentage:", percentage, "%")

    if percentage >= 80:
        print("Excellent performance!")

    elif percentage >= 60:
        print("Good job!")

    elif percentage >= 40:
        print("Keep practicing.")

    else:
        print("You need more practice.")


while True:

    try:

        print("\n========== QUIZ SYSTEM ==========")
        print("1. Start Quiz")
        print("2. Exit")

        choice = int(input("Choice: "))

        if choice == 1:
            start_quiz()

        elif choice == 2:
            print("Thank you for playing.")
            break

        else:
            print("Invalid choice.")

    except ValueError:

        print("Please enter a number.")