bookings = {}

while True:

    try:
        print("\n========== TAXI BOOKING SYSTEM ==========")
        print("1. Book Taxi")
        print("2. View Bookings")
        print("3. Search Booking")
        print("4. Cancel Booking")
        print("5. Exit")

        choice = int(input("Enter Choice: "))

        if choice == 1:

            booking_id = input("Booking ID: ")

            if booking_id in bookings:
                raise Exception("Booking ID already exists.")

            customer = input("Customer Name: ")
            pickup = input("Pickup Location: ")
            destination = input("Destination: ")

            bookings[booking_id] = {
                "Customer": customer,
                "Pickup": pickup,
                "Destination": destination,
                "Status": "Booked"
            }

            print("Taxi Booked Successfully.")

        elif choice == 2:

            if len(bookings) == 0:
                print("No Bookings Available.")

            else:
                for booking_id, data in bookings.items():
                    print("---------------------------")
                    print("Booking ID :", booking_id)
                    print("Customer   :", data["Customer"])
                    print("Pickup     :", data["Pickup"])
                    print("Destination:", data["Destination"])
                    print("Status     :", data["Status"])

        elif choice == 3:

            booking_id = input("Booking ID: ")

            if booking_id not in bookings:
                raise Exception("Booking Not Found.")

            print(bookings[booking_id])

        elif choice == 4:

            booking_id = input("Booking ID: ")

            if booking_id not in bookings:
                raise Exception("Booking Not Found.")

            del bookings[booking_id]

            print("Booking Cancelled Successfully.")

        elif choice == 5:
            print("Thank You!")
            break

        else:
            print("Invalid Choice.")

    except Exception as e:
        print(e)