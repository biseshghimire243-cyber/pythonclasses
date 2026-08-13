cars = {
    1: {"model": "Toyota Corolla", "price": 3000, "available": True},
    2: {"model": "Hyundai Creta", "price": 4000, "available": True},
    3: {"model": "Tesla Model 3", "price": 7000, "available": True}
}

rentals = {}


def view_cars():

    for car_id, car in cars.items():

        status = "Available" if car["available"] else "Rented"

        print(
            car_id,
            "|",
            car["model"],
            "| Rs.",
            car["price"],
            "per day |",
            status
        )


def rent_car():

    car_id = int(input("Enter car ID: "))

    if car_id not in cars:
        raise Exception("Car not found.")

    if not cars[car_id]["available"]:
        raise Exception("Car is already rented.")

    customer = input("Customer name: ")
    days = int(input("Number of days: "))

    if days <= 0:
        raise Exception("Invalid number of days.")

    total = cars[car_id]["price"] * days

    cars[car_id]["available"] = False

    rentals[car_id] = {
        "Customer": customer,
        "Days": days,
        "Total": total
    }

    print("Car rented successfully.")
    print("Total: Rs.", total)


def return_car():

    car_id = int(input("Enter car ID: "))

    if car_id not in rentals:
        raise Exception("Rental not found.")

    cars[car_id]["available"] = True

    del rentals[car_id]

    print("Car returned successfully.")


while True:

    try:

        print("\n========== CAR RENTAL ==========")
        print("1. View Cars")
        print("2. Rent Car")
        print("3. Return Car")
        print("4. Exit")

        choice = int(input("Choice: "))

        if choice == 1:
            view_cars()

        elif choice == 2:
            rent_car()

        elif choice == 3:
            return_car()

        elif choice == 4:
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Enter valid input.")

    except Exception as e:
        print("Error:", e)