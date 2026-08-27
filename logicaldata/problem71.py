students = {
    "Bishesh": 85,
    "Ram": 72,
    "Sita": 91,
    "Hari": 68
}

name = input("Enter student name: ")

if name in students:
    print("Student found")
    print("Marks:", students[name])
else:
    print("Student not found")