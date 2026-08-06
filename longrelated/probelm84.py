students = {}

def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B+"
    elif marks >= 60:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "F"

while True:

    try:
        print("\n========== STUDENT RESULT MANAGEMENT ==========")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Show Grade")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            roll = int(input("Enter Roll Number: "))

            if roll in students:
                raise Exception("Student already exists.")

            name = input("Enter Name: ")
            marks = float(input("Enter Marks: "))

            if marks < 0 or marks > 100:
                raise Exception("Marks must be between 0 and 100.")

            students[roll] = {
                "Name": name,
                "Marks": marks
            }

            print("Student Added Successfully.")

        elif choice == 2:

            if len(students) == 0:
                print("No Student Records Found.")

            else:

                print("\n========== STUDENT LIST ==========")

                for roll, info in students.items():

                    print("-----------------------------")
                    print("Roll :", roll)
                    print("Name :", info["Name"])
                    print("Marks :", info["Marks"])
                    print("Grade :", calculate_grade(info["Marks"]))

        elif choice == 3:

            roll = int(input("Enter Roll Number: "))

            if roll not in students:
                raise Exception("Student not found.")

            info = students[roll]

            print("\nStudent Details")
            print("Roll :", roll)
            print("Name :", info["Name"])
            print("Marks :", info["Marks"])
            print("Grade :", calculate_grade(info["Marks"]))

        elif choice == 4:

            roll = int(input("Enter Roll Number: "))

            if roll not in students:
                raise Exception("Student not found.")

            marks = float(input("Enter New Marks: "))

            if marks < 0 or marks > 100:
                raise Exception("Invalid Marks.")

            students[roll]["Marks"] = marks

            print("Marks Updated Successfully.")

        elif choice == 5:

            roll = int(input("Enter Roll Number: "))

            if roll not in students:
                raise Exception("Student not found.")

            del students[roll]

            print("Student Deleted Successfully.")

        elif choice == 6:

            roll = int(input("Enter Roll Number: "))

            if roll not in students:
                raise Exception("Student not found.")

            grade = calculate_grade(students[roll]["Marks"])

            print("Student:", students[roll]["Name"])
            print("Grade:", grade)

        elif choice == 7:

            print("Thank you for using Student Result Management System.")
            break

        else:
            print("Invalid Choice.")

    except ValueError:
        print("Please enter valid numeric values.")

    except Exception as e:
        print("Error:", e)