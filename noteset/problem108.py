employees = {}


def add_employee():

    employee_id = input("Employee ID: ")

    if employee_id in employees:
        raise Exception("Employee already exists.")

    name = input("Employee Name: ")
    department = input("Department: ")
    salary = float(input("Salary: "))

    if salary <= 0:
        raise Exception("Salary must be greater than zero.")

    employees[employee_id] = {
        "Name": name,
        "Department": department,
        "Salary": salary
    }

    print("Employee added successfully.")


def view_employees():

    if len(employees) == 0:
        print("No employees found.")
        return

    print("\n========== EMPLOYEE LIST ==========")

    for employee_id, employee in employees.items():

        print("-----------------------------")
        print("ID:", employee_id)
        print("Name:", employee["Name"])
        print("Department:", employee["Department"])
        print("Salary:", employee["Salary"])


def search_employee():

    employee_id = input("Employee ID: ")

    if employee_id not in employees:
        raise Exception("Employee not found.")

    print("\nEmployee Details")
    print(employees[employee_id])


def update_salary():

    employee_id = input("Employee ID: ")

    if employee_id not in employees:
        raise Exception("Employee not found.")

    new_salary = float(input("New Salary: "))

    if new_salary <= 0:
        raise Exception("Invalid salary.")

    employees[employee_id]["Salary"] = new_salary

    print("Salary updated successfully.")


def remove_employee():

    employee_id = input("Employee ID: ")

    if employee_id not in employees:
        raise Exception("Employee not found.")

    del employees[employee_id]

    print("Employee removed successfully.")


def total_salary():

    total = 0

    for employee in employees.values():
        total += employee["Salary"]

    print("Total Salary Expense: Rs.", total)


while True:

    try:

        print("\n========== EMPLOYEE MANAGEMENT ==========")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Update Salary")
        print("5. Remove Employee")
        print("6. Total Salary")
        print("7. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            add_employee()

        elif choice == 2:
            view_employees()

        elif choice == 3:
            search_employee()

        elif choice == 4:
            update_salary()

        elif choice == 5:
            remove_employee()

        elif choice == 6:
            total_salary()

        elif choice == 7:
            print("Thank you.")
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Please enter valid input.")

    except Exception as e:
        print("Error:", e)