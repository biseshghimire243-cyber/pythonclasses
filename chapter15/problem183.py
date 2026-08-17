import json
import os


class ManagementSystem:

    def __init__(self):

        self.filename = "management.json"
        self.records = self.load()

    def load(self):

        if not os.path.exists(self.filename):

            return []

        try:

            with open(self.filename, "r") as file:

                return json.load(file)

        except json.JSONDecodeError:

            print("Invalid JSON file.")

            return []

    def save(self):

        with open(self.filename, "w") as file:

            json.dump(
                self.records,
                file,
                indent=4
            )

    def add_record(self):

        record = {

            "id": input("ID: "),
            "name": input("Name: "),
            "email": input("Email: "),
            "phone": input("Phone: ")
        }

        self.records.append(record)

        self.save()

        print("Record added successfully.")

    def search_record(self):

        record_id = input("Enter ID: ")

        for record in self.records:

            if record["id"] == record_id:

                print("\n========== RECORD ==========")
                print("ID:", record["id"])
                print("Name:", record["name"])
                print("Email:", record["email"])
                print("Phone:", record["phone"])

                return

        print("Record not found.")

    def delete_record(self):

        record_id = input("Enter ID: ")

        for record in self.records:

            if record["id"] == record_id:

                self.records.remove(record)

                self.save()

                print("Record deleted.")

                return

        print("Record not found.")

    def display_records(self):

        print("\n========== ALL RECORDS ==========")

        if not self.records:

            print("No records available.")
            return

        for record in self.records:

            print(
                record["id"],
                "|",
                record["name"],
                "|",
                record["email"],
                "|",
                record["phone"]
            )


system = ManagementSystem()

while True:

    print("\n========== MANAGEMENT SYSTEM ==========")
    print("1. Add Record")
    print("2. Search Record")
    print("3. Delete Record")
    print("4. View Records")
    print("5. Exit")

    choice = input("Enter choice: ")

    try:

        if choice == "1":

            system.add_record()

        elif choice == "2":

            system.search_record()

        elif choice == "3":

            system.delete_record()

        elif choice == "4":

            system.display_records()

        elif choice == "5":

            print("Program ended.")
            break

        else:

            print("Invalid choice.")

    except Exception as error:

        print("Error:", error)