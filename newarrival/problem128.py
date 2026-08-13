flights = {
    "NP101": {
        "from": "Kathmandu",
        "to": "Pokhara",
        "price": 5000,
        "seats": 5
    },
    "NP102": {
        "from": "Kathmandu",
        "to": "Biratnagar",
        "price": 6000,
        "seats": 5
    }
}

bookings = []


def show_flights():

    for code, flight in flights.items():

        print(
            code,
            "|",
            flight["from"],
            "to",
            flight["to"],
            "| Rs.",
            flight["price"],
            "| Seats:",
            flight["seats"]
        )


def book_flight():

    code = input("Flight Code: ").upper()

    if code not in flights:
        raise Exception("Flight not found.")

    if flights[code]["seats"] <= 0:
        raise Exception("No seats available.")

    passenger = input("Passenger Name: ")

    flights[code]["seats"] -= 1

    bookings.append({
        "Passenger": passenger,
        "Flight": code
    })

    print("Flight booked successfully.")


def view_bookings():

    if not bookings:
        print("No bookings.")
        return

    for booking in bookings:

        print(
            booking["Passenger"],
            "->",
            booking["Flight"]
        )


while True:

    try:

        print("\n========== FLIGHT BOOKING ==========")
        print("1. Show Flights")
        print("2. Book Flight")
        print("3. View Bookings")
        print("4. Exit")

        choice = int(input("Choice: "))

        if choice == 1:
            show_flights()

        elif choice == 2:
            book_flight()

        elif choice == 3:
            view_bookings()

        elif choice == 4:
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Enter valid input.")

    except Exception as e:
        print("Error:", e)