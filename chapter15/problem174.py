import json
import os


class StudentSystem:

    def __init__(self):
        self.filename = "student_records.json"
        self.students = self.load()

    def load(self):

        if not os.path.exists(self.filename):
            return []

        with open(self.filename, "r") as file:

            return json.load(file)

    def save(self):

        with open(self.filename, "w") as file:

            json.dump(
                self.students,
                file,
                indent=4
            )

    def add_student(self):

        roll = input("Roll Number: ")

        for student in self.students:

            if student["roll"] == roll:

                print("Student already exists.")
                return

        name = input("Name: ")
        course = input("Course: ")

        student = {
            "roll": roll,
            "name": name,
            "course": course
        }

        self.students.append(student)

        self.save()

        print("Student added.")

    def display(self):

        print("\n========== STUDENTS ==========")

        if not self.students:

            print("No records.")
            return

        for student in self.students:

            print(
                "Roll:", student["roll"],
                "| Name:", student["name"],
                "| Course:", student["course"]
            )


system = StudentSystem()

while True:

    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Choice: ")

    if choice == "1":

        system.add_student()

    elif choice == "2":

        system.display()

    elif choice == "3":

        break

    else:

        print("Invalid choice.")