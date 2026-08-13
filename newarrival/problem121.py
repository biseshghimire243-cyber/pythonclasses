seats = {}

for seat in range(1, 21):
    seats[seat] = None


def view_seats():

    print("\n========== SEATS ==========")

    for seat, passenger in seats.items():

        if passenger is None:
            print(seat, "-> Available")
        else:
            print(seat, "->", passenger)


def reserve_seat():

    seat = int(input("Enter seat number: "))

    if seat not in seats:
        raise Exception("Invalid seat number.")

    if seats[seat] is not None:
        raise Exception("Seat already reserved.")

    name = input("Passenger Name: ")

    seats[seat] = name

    print("Seat reserved successfully.")


def cancel_seat():

    seat = int(input("Enter seat number: "))

    if seat not in seats:
        raise Exception("Invalid seat.")

    if seats[seat] is None:
        raise Exception("Seat is already available.")

    seats[seat] = None

    print("Reservation cancelled.")


while True:

    try:

        print("\n========== BUS RESERVATION ==========")
        print("1. View Seats")
        print("2. Reserve Seat")
        print("3. Cancel Reservation")
        print("4. Exit")

        choice = int(input("Choice: "))

        if choice == 1:
            view_seats()

        elif choice == 2:
            reserve_seat()

        elif choice == 3:
            cancel_seat()

        elif choice == 4:
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Enter a valid number.")

    except Exception as e:
        print("Error:", e)