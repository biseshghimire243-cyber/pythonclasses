employees = {}

while True:

    try:
        print("\n========== EMPLOYEE PAYROLL SYSTEM ==========")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Calculate Salary")
        print("4. Search Employee")
        print("5. Delete Employee")
        print("6. Exit")

        choice = int(input("Enter Choice: "))

        if choice == 1:

            emp_id = int(input("Employee ID: "))

            if emp_id in employees:
                raise Exception("Employee already exists.")

            name = input("Employee Name: ")
            hours = float(input("Working Hours: "))
            rate = float(input("Hourly Rate: "))

            employees[emp_id] = {
                "Name": name,
                "Hours": hours,
                "Rate": rate
            }

            print("Employee Added Successfully.")

        elif choice == 2:

            if len(employees) == 0:
                print("No Employee Found.")

            else:
                for emp_id, info in employees.items():
                    print("\nEmployee ID:", emp_id)
                    print("Name:", info["Name"])
                    print("Hours:", info["Hours"])
                    print("Rate:", info["Rate"])

        elif choice == 3:

            emp_id = int(input("Enter Employee ID: "))

            if emp_id not in employees:
                raise Exception("Employee not found.")

            salary = employees[emp_id]["Hours"] * employees[emp_id]["Rate"]

            print("Salary = Rs.", salary)

        elif choice == 4:

            emp_id = int(input("Enter Employee ID: "))

            if emp_id not in employees:
                raise Exception("Employee not found.")

            print(employees[emp_id])

        elif choice == 5:

            emp_id = int(input("Employee ID: "))

            if emp_id not in employees:
                raise Exception("Employee not found.")

            del employees[emp_id]

            print("Employee Deleted.")

        elif choice == 6:
            break

        else:
            print("Invalid Choice")

    except ValueError:
        print("Please enter valid input.")

    except Exception as e:
        print(e)