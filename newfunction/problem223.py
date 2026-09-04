students = []

n = int(input("Enter number of students: "))

for _ in range(n):
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    students.append((name, marks))

students.sort(key=lambda student: (-student[1], student[0]))

print("\nStudents sorted by marks:")
for name, marks in students:
    print(name, "-", marks)