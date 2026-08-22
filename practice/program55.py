name = input("Enter student name: ")

marks = []

for i in range(5):
    mark = float(input("Enter mark: "))
    marks.append(mark)

total = sum(marks)
percentage = total / len(marks)

print("\nStudent:", name)
print("Total:", total)
print("Percentage:", percentage)

if percentage >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")