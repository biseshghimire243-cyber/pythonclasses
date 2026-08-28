students = {
    "Bishesh": 85,
    "Ram": 72,
    "Sita": 91,
    "Hari": 58,
    "Gita": 45
}

grades = {
    "A": [],
    "B": [],
    "C": [],
    "D": []
}

for name, marks in students.items():

    if marks >= 80:
        grades["A"].append(name)
    elif marks >= 70:
        grades["B"].append(name)
    elif marks >= 60:
        grades["C"].append(name)
    else:
        grades["D"].append(name)

for grade, names in grades.items():
    print(grade, ":", names)