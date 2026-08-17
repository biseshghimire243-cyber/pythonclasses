import json
import os


filename = "students.json"


def load_students():

    if not os.path.exists(filename):

        return []

    with open(filename, "r") as file:

        return json.load(file)


def save_students(students):

    with open(filename, "w") as file:

        json.dump(
            students,
            file,
            indent=4
        )


def add_student():

    students = load_students()

    name = input("Name: ")
    roll = input("Roll: ")
    course = input("Course: ")

    student = {
        "name": name,
        "roll": roll,
        "course": course
    }

    students.append(student)

    save_students(students)

    print("Student saved.")


def show_students():

    students = load_students()

    print("\n========== STUDENTS ==========")

    for student in students:

        print(
            student["roll"],
            "|",
            student["name"],
            "|",
            student["course"]
        )


while True:

    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Choice: ")

    if choice == "1":

        add_student()

    elif choice == "2":

        show_students()

    elif choice == "3":

        break

    else:

        print("Invalid choice.")