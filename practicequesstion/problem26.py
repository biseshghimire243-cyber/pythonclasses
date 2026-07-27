try:
    grade = input("Enter grade: ").upper()

    if grade not in ["A", "B", "C", "D", "F"]:
        raise Exception("Invalid grade.")

    print("Grade:", grade)

except Exception as e:
    print(e)