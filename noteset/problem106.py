properties = {}


def add_property():

    property_id = input("Enter Property ID: ")

    if property_id in properties:
        raise Exception("Property already exists.")

    owner = input("Owner Name: ")
    location = input("Location: ")
    property_type = input("Property Type (House/Land/Apartment): ")
    price = float(input("Price: "))

    if price <= 0:
        raise Exception("Price must be greater than zero.")

    properties[property_id] = {
        "Owner": owner,
        "Location": location,
        "Type": property_type,
        "Price": price,
        "Status": "Available"
    }

    print("Property added successfully.")


def view_properties():

    if len(properties) == 0:
        print("No properties available.")
        return

    print("\n========== PROPERTY LIST ==========")

    for property_id, data in properties.items():

        print("-----------------------------")
        print("Property ID:", property_id)
        print("Owner:", data["Owner"])
        print("Location:", data["Location"])
        print("Type:", data["Type"])
        print("Price:", data["Price"])
        print("Status:", data["Status"])


def search_location():

    location = input("Enter location: ").lower()

    found = False

    for property_id, data in properties.items():

        if location in data["Location"].lower():

            print("\nProperty ID:", property_id)
            print("Owner:", data["Owner"])
            print("Location:", data["Location"])
            print("Type:", data["Type"])
            print("Price:", data["Price"])
            print("Status:", data["Status"])

            found = True

    if not found:
        print("No property found in this location.")


def search_price():

    maximum = float(input("Enter maximum price: "))

    found = False

    for property_id, data in properties.items():

        if data["Price"] <= maximum:

            print("\nProperty ID:", property_id)
            print("Location:", data["Location"])
            print("Price:", data["Price"])

            found = True

    if not found:
        print("No property found under this price.")


def sell_property():

    property_id = input("Enter Property ID: ")

    if property_id not in properties:
        raise Exception("Property not found.")

    if properties[property_id]["Status"] == "Sold":
        raise Exception("Property already sold.")

    properties[property_id]["Status"] = "Sold"

    print("Property sold successfully.")


def remove_property():

    property_id = input("Enter Property ID: ")

    if property_id not in properties:
        raise Exception("Property not found.")

    del properties[property_id]

    print("Property removed successfully.")


while True:

    try:

        print("\n========== REAL ESTATE SYSTEM ==========")
        print("1. Add Property")
        print("2. View Properties")
        print("3. Search by Location")
        print("4. Search by Price")
        print("5. Sell Property")
        print("6. Remove Property")
        print("7. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            add_property()

        elif choice == 2:
            view_properties()

        elif choice == 3:
            search_location()

        elif choice == 4:
            search_price()

        elif choice == 5:
            sell_property()

        elif choice == 6:
            remove_property()

        elif choice == 7:
            print("Thank you.")
            break

        else:
            print("Invalid choice.")

    except ValueError:

        print("Please enter valid input.")

    except Exception as e:

        print("Error:", e)