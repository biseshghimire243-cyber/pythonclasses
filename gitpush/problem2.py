students = {}

while True:

    try:

        print("\n========== SCHOOL MANAGEMENT SYSTEM ==========")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = int(input("Enter Choice: "))

        if choice == 1:

            roll = int(input("Roll No: "))

            if roll in students:
                raise Exception("Student Already Exists.")

            name = input("Student Name: ")
            grade = input("Grade: ")

            students[roll] = {
                "Name": name,
                "Grade": grade
            }

            print("Student Added Successfully.")

        elif choice == 2:

            if len(students) == 0:
                print("No Student Records.")

            else:

                for roll, data in students.items():

                    print("-----------------------")
                    print("Roll :", roll)
                    print("Name :", data["Name"])
                    print("Grade :", data["Grade"])

        elif choice == 3:

            roll = int(input("Enter Roll No: "))

            if roll not in students:
                raise Exception("Student Not Found.")

            print(students[roll])

        elif choice == 4:

            roll = int(input("Enter Roll No: "))

            if roll not in students:
                raise Exception("Student Not Found.")

            del students[roll]

            print("Student Deleted Successfully.")

        elif choice == 5:
            break

        else:
            print("Invalid Choice.")

    except Exception as e:
        print(e)