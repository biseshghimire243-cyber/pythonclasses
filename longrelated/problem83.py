rooms = {}

while True:

    try:

        print("\n===== HOTEL MANAGEMENT =====")
        print("1. Book Room")
        print("2. View Bookings")
        print("3. Checkout")
        print("4. Exit")

        choice = int(input("Choice: "))

        if choice == 1:

            room = input("Room Number: ")
            name = input("Customer Name: ")

            rooms[room] = name

            print("Room Booked Successfully.")

        elif choice == 2:

            if len(rooms) == 0:
                print("No Booking.")

            else:

                for room, customer in rooms.items():

                    print("Room", room, "->", customer)

        elif choice == 3:

            room = input("Room Number: ")

            if room not in rooms:
                raise Exception("Room Not Found.")

            del rooms[room]

            print("Checkout Successful.")

        elif choice == 4:
            break

        else:
            print("Invalid Choice")

    except Exception as e:
        print(e)