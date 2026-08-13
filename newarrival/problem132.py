applications = {}


def add_application():

    company = input("Company Name: ")

    if company in applications:
        raise Exception("Application already exists.")

    position = input("Job Position: ")

    applications[company] = {
        "Position": position,
        "Status": "Applied"
    }

    print("Application added.")


def update_status():

    company = input("Company Name: ")

    if company not in applications:
        raise Exception("Application not found.")

    print("\n1. Applied")
    print("2. Interview")
    print("3. Selected")
    print("4. Rejected")

    choice = int(input("Choose status: "))

    statuses = {
        1: "Applied",
        2: "Interview",
        3: "Selected",
        4: "Rejected"
    }

    if choice not in statuses:
        raise Exception("Invalid status.")

    applications[company]["Status"] = statuses[choice]

    print("Status updated.")


def view_applications():

    if not applications:
        print("No applications.")
        return

    print("\n========== JOB APPLICATIONS ==========")

    for company, application in applications.items():

        print(
            company,
            "|",
            application["Position"],
            "|",
            application["Status"]
        )


while True:

    try:

        print("\n========== JOB TRACKER ==========")
        print("1. Add Application")
        print("2. Update Status")
        print("3. View Applications")
        print("4. Exit")

        choice = int(input("Choice: "))

        if choice == 1:
            add_application()

        elif choice == 2:
            update_status()

        elif choice == 3:
            view_applications()

        elif choice == 4:
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Enter valid input.")

    except Exception as e:
        print("Error:", e)