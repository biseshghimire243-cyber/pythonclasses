class Event:

    def __init__(self, name, date, capacity):
        self.name = name
        self.date = date
        self.capacity = capacity
        self.attendees = []

    def register(self, person):

        if len(self.attendees) >= self.capacity:
            raise ValueError("Event is full.")

        if person in self.attendees:
            raise ValueError("Already registered.")

        self.attendees.append(person)

        print("Registration successful.")

    def show_event(self):

        print("\n========== EVENT ==========")
        print("Event:", self.name)
        print("Date:", self.date)
        print(
            "Seats:",
            len(self.attendees),
            "/",
            self.capacity
        )

        print("\nAttendees:")

        for person in self.attendees:
            print("-", person)


event = Event(
    "Python Workshop",
    "2026-09-10",
    5
)

while True:

    try:

        print("\n1. Register")
        print("2. View Event")
        print("3. Exit")

        choice = int(input("Choice: "))

        if choice == 1:

            name = input("Your Name: ")

            event.register(name)

        elif choice == 2:

            event.show_event()

        elif choice == 3:
            break

        else:
            print("Invalid choice.")

    except ValueError as e:
        print("Error:", e)