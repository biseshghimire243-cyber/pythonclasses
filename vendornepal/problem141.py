class Room:

    def __init__(self, room_number, price):

        self.room_number = room_number
        self.__price = price
        self.__booked = False

    def book(self):

        if self.__booked:
            raise Exception("Room already booked.")

        self.__booked = True

        print("Room booked successfully.")

    def checkout(self):

        if not self.__booked:
            raise Exception("Room is not booked.")

        self.__booked = False

        print("Checkout completed.")

    def show_room(self):

        status = "Booked" if self.__booked else "Available"

        print(
            "Room:",
            self.room_number,
            "| Price:",
            self.__price,
            "| Status:",
            status
        )


rooms = [
    Room(101, 2000),
    Room(102, 3000),
    Room(103, 5000)
]


while True:

    print("\n========== HOTEL ==========")
    print("1. View Rooms")
    print("2. Book Room")
    print("3. Checkout")
    print("4. Exit")

    choice = input("Choice: ")

    try:

        if choice == "1":

            for room in rooms:
                room.show_room()

        elif choice == "2":

            number = int(input("Room number: "))

            for room in rooms:

                if room.room_number == number:

                    room.book()
                    break

            else:
                print("Room not found.")

        elif choice == "3":

            number = int(input("Room number: "))

            for room in rooms:

                if room.room_number == number:

                    room.checkout()
                    break

            else:
                print("Room not found.")

        elif choice == "4":

            break

        else:

            print("Invalid choice.")

    except Exception as e:

        print("Error:", e)