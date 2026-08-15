class Property:

    def __init__(self, property_id, location, price):
        self.property_id = property_id
        self.location = location
        self.price = price
        self.sold = False

    def sell(self):

        if self.sold:
            raise ValueError("Property already sold.")

        self.sold = True

        print("Property sold successfully.")

    def show(self):

        status = "Sold" if self.sold else "Available"

        print(
            self.property_id,
            "|",
            self.location,
            "| Rs.",
            self.price,
            "|",
            status
        )


properties = {}

while True:

    try:

        print("\n1. Add Property")
        print("2. View Properties")
        print("3. Sell Property")
        print("4. Exit")

        choice = int(input("Choice: "))

        if choice == 1:

            property_id = input("Property ID: ")

            if property_id in properties:
                raise ValueError("Property already exists.")

            location = input("Location: ")
            price = float(input("Price: "))

            properties[property_id] = Property(
                property_id,
                location,
                price
            )

            print("Property added.")

        elif choice == 2:

            for property in properties.values():
                property.show()

        elif choice == 3:

            property_id = input("Property ID: ")

            if property_id not in properties:
                raise ValueError("Property not found.")

            properties[property_id].sell()

        elif choice == 4:
            break

        else:
            print("Invalid choice.")

    except ValueError as e:
        print("Error:", e)