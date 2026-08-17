import json
import os


class ContactManager:

    def __init__(self):

        self.filename = "contacts.json"
        self.contacts = self.load_contacts()

    def load_contacts(self):

        if not os.path.exists(self.filename):
            return []

        with open(self.filename, "r") as file:

            return json.load(file)

    def save_contacts(self):

        with open(self.filename, "w") as file:

            json.dump(
                self.contacts,
                file,
                indent=4
            )

    def add_contact(self):

        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")

        contact = {
            "name": name,
            "phone": phone,
            "email": email
        }

        self.contacts.append(contact)

        self.save_contacts()

        print("Contact added.")

    def search(self):

        name = input("Enter name to search: ")

        for contact in self.contacts:

            if contact["name"].lower() == name.lower():

                print("\nName:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])

                return

        print("Contact not found.")

    def display(self):

        print("\n========== CONTACTS ==========")

        for contact in self.contacts:

            print(
                contact["name"],
                "|",
                contact["phone"],
                "|",
                contact["email"]
            )


manager = ContactManager()

while True:

    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. View Contacts")
    print("4. Exit")

    choice = input("Choice: ")

    if choice == "1":

        manager.add_contact()

    elif choice == "2":

        manager.search()

    elif choice == "3":

        manager.display()

    elif choice == "4":

        break

    else:

        print("Invalid choice.")