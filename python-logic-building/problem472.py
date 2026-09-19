students = int(input("Enter number of students: "))

for i in range(students):
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))

    if marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    else:
        grade = "F"

    print(name, "->", grade)