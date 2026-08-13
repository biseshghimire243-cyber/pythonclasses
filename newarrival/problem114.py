rooms = {
    101: {"type": "Single", "price": 2000, "available": True},
    102: {"type": "Double", "price": 3500, "available": True},
    103: {"type": "Deluxe", "price": 5000, "available": True}
}

bookings = {}


def view_rooms():
    print("\n========== ROOMS ==========")

    for room, data in rooms.items():
        status = "Available" if data["available"] else "Booked"

        print(
            room,
            "|",
            data["type"],
            "| Rs.",
            data["price"],
            "|",
            status
        )


def book_room():

    room = int(input("Enter room number: "))

    if room not in rooms:
        raise Exception("Room not found.")

    if not rooms[room]["available"]:
        raise Exception("Room is already booked.")

    name = input("Guest name: ")
    nights = int(input("Number of nights: "))

    if nights <= 0:
        raise Exception("Invalid number of nights.")

    total = rooms[room]["price"] * nights

    rooms[room]["available"] = False

    bookings[room] = {
        "Guest": name,
        "Nights": nights,
        "Total": total
    }

    print("Room booked successfully.")
    print("Total: Rs.", total)


def checkout():

    room = int(input("Enter room number: "))

    if room not in bookings:
        raise Exception("No booking found.")

    booking = bookings[room]

    print("\n========== CHECKOUT ==========")
    print("Guest:", booking["Guest"])
    print("Nights:", booking["Nights"])
    print("Total:", booking["Total"])

    rooms[room]["available"] = True

    del bookings[room]

    print("Checkout completed.")


while True:

    try:
        print("\n========== HOTEL SYSTEM ==========")
        print("1. View Rooms")
        print("2. Book Room")
        print("3. Checkout")
        print("4. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            view_rooms()

        elif choice == 2:
            book_room()

        elif choice == 3:
            checkout()

        elif choice == 4:
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Enter a valid number.")

    except Exception as e:
        print("Error:", e)