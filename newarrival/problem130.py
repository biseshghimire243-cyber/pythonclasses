contacts = {}


def add_contact():

    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")

    contacts[name] = {
        "Phone": phone,
        "Email": email
    }

    print("Contact saved.")


def search_contact():

    name = input("Search name: ")

    if name not in contacts:
        print("Contact not found.")
        return

    print("\nName:", name)
    print("Phone:", contacts[name]["Phone"])
    print("Email:", contacts[name]["Email"])


def delete_contact():

    name = input("Name: ")

    if name not in contacts:
        raise Exception("Contact not found.")

    del contacts[name]

    print("Contact deleted.")


def view_contacts():

    if not contacts:
        print("No contacts.")

        return

    print("\n========== CONTACTS ==========")

    for name, contact in contacts.items():

        print(
            name,
            "|",
            contact["Phone"],
            "|",
            contact["Email"]
        )


while True:

    try:

        print("\n========== CONTACT MANAGER ==========")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. View Contacts")
        print("5. Exit")

        choice = int(input("Choice: "))

        if choice == 1:
            add_contact()

        elif choice == 2:
            search_contact()

        elif choice == 3:
            delete_contact()

        elif choice == 4:
            view_contacts()

        elif choice == 5:
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Enter valid input.")

    except Exception as e:
        print("Error:", e)