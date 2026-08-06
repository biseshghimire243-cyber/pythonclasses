students = {}

while True:

    try:

        print("\n========== STUDENT MANAGEMENT ==========")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = int(input("Enter Choice : "))

        if choice == 1:

            roll = int(input("Roll No : "))

            if roll in students:
                raise Exception("Student Already Exists.")

            name = input("Name : ")
            age = int(input("Age : "))
            marks = float(input("Marks : "))

            students[roll] = {
                "Name": name,
                "Age": age,
                "Marks": marks
            }

            print("Student Added Successfully.")

        elif choice == 2:

            if len(students) == 0:
                print("No Student Found.")

            else:

                print("\n===== STUDENT LIST =====")

                for roll, info in students.items():

                    print("-------------------------")
                    print("Roll :", roll)
                    print("Name :", info["Name"])
                    print("Age :", info["Age"])
                    print("Marks :", info["Marks"])

        elif choice == 3:

            roll = int(input("Enter Roll No : "))

            if roll not in students:
                raise Exception("Student Not Found.")

            print(students[roll])

        elif choice == 4:

            roll = int(input("Enter Roll No : "))

            if roll not in students:
                raise Exception("Student Not Found.")

            students[roll]["Marks"] = float(
                input("Enter New Marks : ")
            )

            print("Record Updated.")

        elif choice == 5:

            roll = int(input("Enter Roll No : "))

            if roll not in students:
                raise Exception("Student Not Found.")

            del students[roll]

            print("Student Deleted.")

        elif choice == 6:
            print("Program Closed.")
            break

        else:
            print("Invalid Choice.")

    except ValueError:
        print("Please Enter Valid Input.")

    except Exception as e:
        print(e)