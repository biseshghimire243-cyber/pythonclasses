courses = {
    "CS101": {"name": "Python Programming", "capacity": 3, "students": []},
    "CS102": {"name": "Database Systems", "capacity": 3, "students": []},
    "CS103": {"name": "Web Development", "capacity": 2, "students": []}
}


def show_courses():

    print("\n========== COURSES ==========")

    for code, course in courses.items():

        available = course["capacity"] - len(course["students"])

        print("----------------------------")
        print("Code:", code)
        print("Course:", course["name"])
        print("Available Seats:", available)


def register_student():

    code = input("Enter course code: ").upper()

    if code not in courses:
        raise Exception("Course not found.")

    if len(courses[code]["students"]) >= courses[code]["capacity"]:
        raise Exception("Course is full.")

    name = input("Student Name: ")

    if name in courses[code]["students"]:
        raise Exception("Student already registered.")

    courses[code]["students"].append(name)

    print("Registration successful.")


def view_registrations():

    for code, course in courses.items():

        print("\n", code, "-", course["name"])

        if not course["students"]:
            print("No students registered.")

        else:

            for student in course["students"]:
                print("-", student)


while True:

    try:

        print("\n========== COURSE REGISTRATION ==========")
        print("1. Show Courses")
        print("2. Register Student")
        print("3. View Registrations")
        print("4. Exit")

        choice = int(input("Choice: "))

        if choice == 1:
            show_courses()

        elif choice == 2:
            register_student()

        elif choice == 3:
            view_registrations()

        elif choice == 4:
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Enter a valid number.")

    except Exception as e:
        print("Error:", e)