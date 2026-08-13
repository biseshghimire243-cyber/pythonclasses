from collections import deque

patients = deque()


def add_patient():

    name = input("Patient Name: ")
    age = int(input("Age: "))
    problem = input("Medical Problem: ")

    patients.append({
        "Name": name,
        "Age": age,
        "Problem": problem
    })

    print("Patient added to queue.")


def call_patient():

    if not patients:
        print("No patients waiting.")
        return

    patient = patients.popleft()

    print("\n========== NEXT PATIENT ==========")
    print("Name:", patient["Name"])
    print("Age:", patient["Age"])
    print("Problem:", patient["Problem"])


def view_queue():

    if not patients:
        print("Queue is empty.")
        return

    print("\n========== PATIENT QUEUE ==========")

    for number, patient in enumerate(patients, start=1):

        print(
            number,
            "|",
            patient["Name"],
            "| Age:",
            patient["Age"],
            "|",
            patient["Problem"]
        )


while True:

    try:

        print("\n========== HOSPITAL QUEUE ==========")
        print("1. Add Patient")
        print("2. Call Next Patient")
        print("3. View Queue")
        print("4. Exit")

        choice = int(input("Choice: "))

        if choice == 1:
            add_patient()

        elif choice == 2:
            call_patient()

        elif choice == 3:
            view_queue()

        elif choice == 4:
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Enter valid input.")