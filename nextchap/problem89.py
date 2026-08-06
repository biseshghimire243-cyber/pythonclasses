contacts = {}

while True:

    try:

        print("\n========== CONTACT MANAGEMENT ==========")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = int(input("Choice: "))

        if choice == 1:

            name = input("Name: ")

            if name in contacts:
                raise Exception("Contact Already Exists.")

            phone = input("Phone Number: ")

            contacts[name] = phone

            print("Contact Saved.")

        elif choice == 2:

            if len(contacts) == 0:
                print("No Contacts.")

            else:

                for name, phone in contacts.items():

                    print(name, ":", phone)

        elif choice == 3:

            name = input("Enter Name: ")

            if name not in contacts:
                raise Exception("Contact Not Found.")

            print("Phone:", contacts[name])

        elif choice == 4:

            name = input("Enter Name: ")

            if name not in contacts:
                raise Exception("Contact Not Found.")

            contacts[name] = input("New Number: ")

            print("Updated Successfully.")

        elif choice == 5:

            name = input("Enter Name: ")

            if name not in contacts:
                raise Exception("Contact Not Found.")

            del contacts[name]

            print("Deleted Successfully.")

        elif choice == 6:

            break

        else:

            print("Invalid Choice.")

    except Exception as e:
        print(e)