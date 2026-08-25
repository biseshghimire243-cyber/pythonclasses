name = input("Enter student name: ")

marks = []

for i in range(5):
    mark = float(input(f"Enter subject {i + 1} marks: "))
    marks.append(mark)

total = sum(marks)
percentage = total / 5

print("\nStudent:", name)
print("Total:", total)
print("Percentage:", percentage)

if percentage >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")