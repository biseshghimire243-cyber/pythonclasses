students = {}


def add_student():

    roll = input("Enter Roll Number: ")

    if roll in students:
        raise Exception("Student already exists.")

    name = input("Student Name: ")

    students[roll] = {
        "Name": name,
        "Present": 0,
        "Absent": 0
    }

    print("Student added successfully.")


def mark_attendance():

    roll = input("Enter Roll Number: ")

    if roll not in students:
        raise Exception("Student not found.")

    print("\n1. Present")
    print("2. Absent")

    status = int(input("Enter Status: "))

    if status == 1:

        students[roll]["Present"] += 1

        print("Marked Present.")

    elif status == 2:

        students[roll]["Absent"] += 1

        print("Marked Absent.")

    else:

        raise Exception("Invalid attendance status.")


def view_attendance():

    if len(students) == 0:
        print("No students available.")
        return

    print("\n========== ATTENDANCE ==========")

    for roll, student in students.items():

        total = student["Present"] + student["Absent"]

        if total > 0:
            percentage = (student["Present"] / total) * 100
        else:
            percentage = 0

        print("-----------------------------")
        print("Roll:", roll)
        print("Name:", student["Name"])
        print("Present:", student["Present"])
        print("Absent:", student["Absent"])
        print("Attendance:", round(percentage, 2), "%")


def search_student():

    roll = input("Enter Roll Number: ")

    if roll not in students:
        raise Exception("Student not found.")

    student = students[roll]

    total = student["Present"] + student["Absent"]

    if total > 0:
        percentage = (student["Present"] / total) * 100
    else:
        percentage = 0

    print("\nStudent:", student["Name"])
    print("Present:", student["Present"])
    print("Absent:", student["Absent"])
    print("Attendance:", round(percentage, 2), "%")


while True:

    try:

        print("\n========== ATTENDANCE SYSTEM ==========")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. View Attendance")
        print("4. Search Student")
        print("5. Exit")

        choice = int(input("Enter Choice: "))

        if choice == 1:
            add_student()

        elif choice == 2:
            mark_attendance()

        elif choice == 3:
            view_attendance()

        elif choice == 4:
            search_student()

        elif choice == 5:
            print("Thank you.")
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Please enter valid input.")

    except Exception as e:
        print("Error:", e)