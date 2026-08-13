students = {}


def calculate_grade(percentage):

    if percentage >= 80:
        return "A"

    elif percentage >= 70:
        return "B"

    elif percentage >= 60:
        return "C"

    elif percentage >= 50:
        return "D"

    else:
        return "F"


def add_student():

    roll = input("Roll Number: ")

    if roll in students:
        raise Exception("Student already exists.")

    name = input("Student Name: ")

    marks = []

    for i in range(5):

        mark = float(input(f"Enter marks for subject {i + 1}: "))

        if mark < 0 or mark > 100:
            raise Exception("Marks must be between 0 and 100.")

        marks.append(mark)

    total = sum(marks)
    percentage = total / 5
    grade = calculate_grade(percentage)

    students[roll] = {
        "Name": name,
        "Marks": marks,
        "Total": total,
        "Percentage": percentage,
        "Grade": grade
    }

    print("Student added successfully.")


def view_students():

    for roll, student in students.items():

        print("\n--------------------------")
        print("Roll:", roll)
        print("Name:", student["Name"])
        print("Marks:", student["Marks"])
        print("Total:", student["Total"])
        print("Percentage:", student["Percentage"])
        print("Grade:", student["Grade"])


while True:

    try:

        print("\n========== GRADE SYSTEM ==========")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")

        choice = int(input("Choice: "))

        if choice == 1:
            add_student()

        elif choice == 2:
            view_students()

        elif choice == 3:
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Enter valid input.")

    except Exception as e:
        print("Error:", e)