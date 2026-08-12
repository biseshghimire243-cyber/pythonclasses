bicycles = {
    1: {
        "Name": "Mountain Bike",
        "Price": 200,
        "Available": True
    },
    2: {
        "Name": "Road Bike",
        "Price": 300,
        "Available": True
    },
    3: {
        "Name": "Electric Bike",
        "Price": 500,
        "Available": True
    }
}

rentals = {}


def view_bicycles():

    print("\n========== BICYCLES ==========")

    for bike_id, bike in bicycles.items():

        status = "Available" if bike["Available"] else "Rented"

        print("-----------------------------")
        print("ID:", bike_id)
        print("Name:", bike["Name"])
        print("Price/Hour:", bike["Price"])
        print("Status:", status)


def rent_bicycle():

    bike_id = int(input("Enter Bicycle ID: "))

    if bike_id not in bicycles:
        raise Exception("Bicycle not found.")

    if not bicycles[bike_id]["Available"]:
        raise Exception("Bicycle is already rented.")

    customer = input("Customer Name: ")
    hours = int(input("Number of Hours: "))

    if hours <= 0:
        raise Exception("Invalid number of hours.")

    total = bicycles[bike_id]["Price"] * hours

    bicycles[bike_id]["Available"] = False

    rental_id = "R" + str(len(rentals) + 1)

    rentals[rental_id] = {
        "Customer": customer,
        "Bike": bicycles[bike_id]["Name"],
        "Bike ID": bike_id,
        "Hours": hours,
        "Total": total
    }

    print("\nBicycle rented successfully.")
    print("Rental ID:", rental_id)
    print("Total Cost: Rs.", total)


def return_bicycle():

    rental_id = input("Rental ID: ")

    if rental_id not in rentals:
        raise Exception("Rental record not found.")

    bike_id = rentals[rental_id]["Bike ID"]

    bicycles[bike_id]["Available"] = True

    del rentals[rental_id]

    print("Bicycle returned successfully.")


def view_rentals():

    if len(rentals) == 0:
        print("No active rentals.")
        return

    print("\n========== ACTIVE RENTALS ==========")

    for rental_id, rental in rentals.items():

        print("-----------------------------")
        print("Rental ID:", rental_id)
        print("Customer:", rental["Customer"])
        print("Bike:", rental["Bike"])
        print("Hours:", rental["Hours"])
        print("Total:", rental["Total"])


while True:

    try:

        print("\n========== BICYCLE RENTAL SYSTEM ==========")
        print("1. View Bicycles")
        print("2. Rent Bicycle")
        print("3. Return Bicycle")
        print("4. View Rentals")
        print("5. Exit")

        choice = int(input("Enter Choice: "))

        if choice == 1:
            view_bicycles()

        elif choice == 2:
            rent_bicycle()

        elif choice == 3:
            return_bicycle()

        elif choice == 4:
            view_rentals()

        elif choice == 5:
            print("Thank you.")
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Enter a valid number.")

    except Exception as e:
        print("Error:", e)