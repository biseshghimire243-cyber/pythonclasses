cars = {
    "Toyota": True,
    "Hyundai": True,
    "Honda": True,
    "Suzuki": True
}

rentals = {}

while True:
    try:
        print("\n========== CAR RENTAL SYSTEM ==========")
        print("1. View Cars")
        print("2. Rent Car")
        print("3. Return Car")
        print("4. View Rentals")
        print("5. Exit")

        choice = int(input("Enter Choice: "))

        if choice == 1:
            for car, available in cars.items():
                status = "Available" if available else "Rented"
                print(car, "-", status)

        elif choice == 2:
            car = input("Car Name: ")

            if car not in cars:
                raise Exception("Car Not Found.")

            if not cars[car]:
                raise Exception("Car Already Rented.")

            customer = input("Customer Name: ")

            cars[car] = False
            rentals[car] = customer

            print("Car Rented Successfully.")

        elif choice == 3:
            car = input("Car Name: ")

            if car not in rentals:
                raise Exception("Rental Record Not Found.")

            cars[car] = True
            del rentals[car]

            print("Car Returned Successfully.")

        elif choice == 4:
            print(rentals)

        elif choice == 5:
            break

        else:
            print("Invalid Choice.")

    except Exception as e:
        print(e)