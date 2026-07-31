try:
    score = int(input("Enter exam score: "))

    if score < 0 or score > 100:
        raise Exception("Invalid exam score.")

    print("Score:", score)

except Exception as e:
    print(e)