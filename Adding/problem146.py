class Vehicle:

    def __init__(self, number, owner, model):
        self.number = number
        self.owner = owner
        self.model = model
        self.services = []

    def add_service(self, service, cost):

        if cost <= 0:
            raise ValueError("Invalid service cost.")

        self.services.append({
            "Service": service,
            "Cost": cost
        })

        print("Service added.")

    def show_history(self):

        print("\n========== SERVICE HISTORY ==========")
        print("Vehicle:", self.model)
        print("Number:", self.number)
        print("Owner:", self.owner)

        total = 0

        for service in self.services:

            print(
                service["Service"],
                "- Rs.",
                service["Cost"]
            )

            total += service["Cost"]

        print("--------------------------")
        print("Total Cost: Rs.", total)


vehicles = {}

while True:

    try:

        print("\n1. Add Vehicle")
        print("2. Add Service")
        print("3. Service History")
        print("4. Exit")

        choice = int(input("Choice: "))

        if choice == 1:

            number = input("Vehicle Number: ")

            if number in vehicles:
                raise ValueError("Vehicle already exists.")

            owner = input("Owner Name: ")
            model = input("Vehicle Model: ")

            vehicles[number] = Vehicle(
                number,
                owner,
                model
            )

            print("Vehicle added.")

        elif choice == 2:

            number = input("Vehicle Number: ")

            if number not in vehicles:
                raise ValueError("Vehicle not found.")

            service = input("Service Name: ")
            cost = float(input("Cost: "))

            vehicles[number].add_service(
                service,
                cost
            )

        elif choice == 3:

            number = input("Vehicle Number: ")

            if number not in vehicles:
                raise ValueError("Vehicle not found.")

            vehicles[number].show_history()

        elif choice == 4:
            break

        else:
            print("Invalid choice.")

    except ValueError as e:
        print("Error:", e)