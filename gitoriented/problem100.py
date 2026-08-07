students = {}

while True:

    try:

        print("\n========== COLLEGE ADMISSION ==========")
        print("1. Apply for Admission")
        print("2. View Applications")
        print("3. Search Student")
        print("4. Cancel Admission")
        print("5. Exit")

        choice = int(input("Choice: "))

        if choice == 1:

            student_id = input("Student ID: ")

            if student_id in students:
                raise Exception("Application Already Exists.")

            name = input("Student Name: ")
            course = input("Course: ")

            students[student_id] = {
                "Name": name,
                "Course": course
            }

            print("Admission Application Submitted.")

        elif choice == 2:

            for sid, info in students.items():

                print(sid, info)

        elif choice == 3:

            sid = input("Student ID: ")

            if sid not in students:
                raise Exception("Student Not Found.")

            print(students[sid])

        elif choice == 4:

            sid = input("Student ID: ")

            if sid not in students:
                raise Exception("Student Not Found.")

            del students[sid]

            print("Admission Cancelled.")

        elif choice == 5:
            break

    except Exception as e:
        print(e)