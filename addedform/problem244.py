marks = list(map(int, input("Enter marks: ").split()))

grades = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0,
    "F": 0
}

for mark in marks:
    if mark >= 80:
        grades["A"] += 1
    elif mark >= 70:
        grades["B"] += 1
    elif mark >= 60:
        grades["C"] += 1
    elif mark >= 40:
        grades["D"] += 1
    else:
        grades["F"] += 1

print("Grade distribution:")

for grade, count in grades.items():
    print(grade, ":", count)