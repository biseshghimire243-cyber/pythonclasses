filename = "students.txt"


def add_student():

    name = input("Student Name: ")
    roll = input("Roll Number: ")
    course = input("Course: ")

    with open(filename, "a") as file:

        file.write(
            f"{roll},{name},{course}\n"
        )

    print("Student added successfully.")


def display_students():

    try:

        with open(filename, "r") as file:

            records = file.readlines()

        if not records:

            print("No students found.")
            return

        print("\n========== STUDENTS ==========")

        for record in records:

            roll, name, course = (
                record.strip().split(",")
            )

            print(
                "Roll:", roll,
                "| Name:", name,
                "| Course:", course
            )

    except FileNotFoundError:

        print("No student file found.")


while True:

    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Choice: ")

    if choice == "1":

        add_student()

    elif choice == "2":

        display_students()

    elif choice == "3":

        break

    else:

        print("Invalid choice.")