patients = {}

while True:

    try:
        print("\n========== HOSPITAL MANAGEMENT ==========")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Search Patient")
        print("4. Delete Patient")
        print("5. Exit")

        choice = int(input("Enter Choice: "))

        if choice == 1:

            patient_id = int(input("Patient ID: "))

            if patient_id in patients:
                raise Exception("Patient Already Exists.")

            name = input("Patient Name: ")
            disease = input("Disease: ")
            age = int(input("Age: "))

            patients[patient_id] = {
                "Name": name,
                "Disease": disease,
                "Age": age
            }

            print("Patient Added Successfully.")

        elif choice == 2:

            if len(patients) == 0:
                print("No Patients Found.")

            else:

                for pid, info in patients.items():
                    print("\nPatient ID:", pid)
                    print("Name:", info["Name"])
                    print("Disease:", info["Disease"])
                    print("Age:", info["Age"])

        elif choice == 3:

            patient_id = int(input("Enter Patient ID: "))

            if patient_id not in patients:
                raise Exception("Patient Not Found.")

            print(patients[patient_id])

        elif choice == 4:

            patient_id = int(input("Enter Patient ID: "))

            if patient_id not in patients:
                raise Exception("Patient Not Found.")

            del patients[patient_id]

            print("Patient Deleted.")

        elif choice == 5:
            print("Program Closed.")
            break

        else:
            print("Invalid Choice.")

    except ValueError:
        print("Invalid Input.")

    except Exception as e:
        print(e)