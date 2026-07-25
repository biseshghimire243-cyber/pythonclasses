marks = int(input("Enter marks: "))

if marks > 100:
    raise ValueError("Marks cannot be greater than 100.")

print("Marks =", marks)