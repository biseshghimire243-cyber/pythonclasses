student = {
    "name": "Bishesh",
    "age": 23,
    "course": "B.Sc. CSIT",
    "semester": 7
}

print("Student Information")

for key, value in student.items():
    print(key.title(), ":", value)