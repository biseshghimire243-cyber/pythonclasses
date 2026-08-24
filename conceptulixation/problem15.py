student = {}

student["name"] = input("Enter name: ")
student["age"] = int(input("Enter age: "))
student["course"] = input("Enter course: ")
student["semester"] = int(input("Enter semester: "))

print("\n===== STUDENT INFORMATION =====")

for key, value in student.items():
    print(key.title(), ":", value)