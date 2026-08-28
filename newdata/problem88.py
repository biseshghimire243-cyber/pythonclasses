students = {
    "Bishesh": 85,
    "Ram": 78
}

new_students = {
    "Sita": 92,
    "Hari": 74
}

merged = {}

merged.update(students)
merged.update(new_students)

print("Merged Dictionary:")

for name, marks in merged.items():
    print(name, ":", marks)