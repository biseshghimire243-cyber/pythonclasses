flights = {
    "Kathmandu-Pokhara": 20,
    "Kathmandu-Dharan": 15,
    "Kathmandu-Biratnagar": 10
}

bookings = {}

while True:
    try:
        print("\n========== FLIGHT RESERVATION SYSTEM ==========")
        print("1. View Flights")
        print("2. Book Ticket")
        print("3. Cancel Ticket")
        print("4. View Bookings")
        print("5. Exit")

        choice = int(input("Enter Choice: "))

        if choice == 1:
            for flight, seats in flights.items():
                print(f"{flight} -> {seats} Seats Available")

        elif choice == 2:
            flight = input("Flight Name: ")

            if flight not in flights:
                raise Exception("Flight Not Found.")

            seats = int(input("Number of Seats: "))

            if seats <= 0:
                raise Exception("Invalid Seat Number.")

            if seats > flights[flight]:
                raise Exception("Seats Not Available.")

            flights[flight] -= seats
            bookings[flight] = bookings.get(flight, 0) + seats

            print("Flight Booked Successfully.")

        elif choice == 3:
            flight = input("Flight Name: ")

            if flight not in bookings:
                raise Exception("Booking Not Found.")

            flights[flight] += bookings[flight]
            del bookings[flight]

            print("Booking Cancelled.")

        elif choice == 4:
            print(bookings)

        elif choice == 5:
            break

        else:
            print("Invalid Choice.")

    except Exception as e:
        print(e)