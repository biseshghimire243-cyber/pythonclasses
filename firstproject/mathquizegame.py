import random

def math_quiz():

    score = 0

    for i in range(5):

        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)

        print("\nQuestion", i + 1)

        answer = int(input(f"{num1} + {num2} = "))

        if answer == num1 + num2:
            print("Correct!")
            score += 1

        else:
            print("Wrong!")
            print("Correct Answer:", num1 + num2)

    print("\nFinal Score:", score, "/5")

math_quiz()