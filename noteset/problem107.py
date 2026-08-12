events = {}
bookings = {}


def add_event():
    event_id = input("Enter Event ID: ")

    if event_id in events:
        raise Exception("Event already exists.")

    name = input("Event Name: ")
    venue = input("Venue: ")
    price = float(input("Ticket Price: "))
    seats = int(input("Number of Seats: "))

    if price <= 0 or seats <= 0:
        raise Exception("Price and seats must be positive.")

    events[event_id] = {
        "Name": name,
        "Venue": venue,
        "Price": price,
        "Seats": seats
    }

    print("Event added successfully.")


def view_events():

    if len(events) == 0:
        print("No events available.")
        return

    print("\n========== EVENTS ==========")

    for event_id, event in events.items():

        print("-----------------------------")
        print("ID:", event_id)
        print("Name:", event["Name"])
        print("Venue:", event["Venue"])
        print("Price:", event["Price"])
        print("Available Seats:", event["Seats"])


def book_ticket():

    event_id = input("Enter Event ID: ")

    if event_id not in events:
        raise Exception("Event not found.")

    quantity = int(input("Number of tickets: "))

    if quantity <= 0:
        raise Exception("Invalid ticket quantity.")

    if quantity > events[event_id]["Seats"]:
        raise Exception("Not enough seats.")

    customer = input("Customer Name: ")

    booking_id = "B" + str(len(bookings) + 1)

    total = quantity * events[event_id]["Price"]

    events[event_id]["Seats"] -= quantity

    bookings[booking_id] = {
        "Customer": customer,
        "Event": events[event_id]["Name"],
        "Quantity": quantity,
        "Total": total
    }

    print("\nBooking Successful!")
    print("Booking ID:", booking_id)
    print("Total Amount: Rs.", total)


def cancel_booking():

    booking_id = input("Booking ID: ")

    if booking_id not in bookings:
        raise Exception("Booking not found.")

    booking = bookings[booking_id]

    for event_id, event in events.items():

        if event["Name"] == booking["Event"]:
            event["Seats"] += booking["Quantity"]
            break

    del bookings[booking_id]

    print("Booking cancelled successfully.")


def view_bookings():

    if len(bookings) == 0:
        print("No bookings found.")
        return

    print("\n========== BOOKINGS ==========")

    for booking_id, booking in bookings.items():

        print("-----------------------------")
        print("Booking ID:", booking_id)
        print("Customer:", booking["Customer"])
        print("Event:", booking["Event"])
        print("Tickets:", booking["Quantity"])
        print("Total:", booking["Total"])


while True:

    try:

        print("\n========== EVENT TICKET SYSTEM ==========")
        print("1. Add Event")
        print("2. View Events")
        print("3. Book Ticket")
        print("4. Cancel Booking")
        print("5. View Bookings")
        print("6. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            add_event()

        elif choice == 2:
            view_events()

        elif choice == 3:
            book_ticket()

        elif choice == 4:
            cancel_booking()

        elif choice == 5:
            view_bookings()

        elif choice == 6:
            print("Thank you.")
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Please enter valid input.")

    except Exception as e:
        print("Error:", e)