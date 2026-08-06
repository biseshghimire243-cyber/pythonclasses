seats = [1,2,3,4,5,6,7,8,9,10]
reserved = []

while True:

    try:

        print("\n========== BUS RESERVATION ==========")
        print("1. View Available Seats")
        print("2. Book Seat")
        print("3. Cancel Booking")
        print("4. View Reserved Seats")
        print("5. Exit")

        choice = int(input("Enter Choice: "))

        if choice == 1:

            print("Available Seats:", seats)

        elif choice == 2:

            seat = int(input("Enter Seat Number: "))

            if seat not in seats:
                raise Exception("Seat Not Available.")

            seats.remove(seat)
            reserved.append(seat)

            print("Seat Booked Successfully.")

        elif choice == 3:

            seat = int(input("Enter Seat Number: "))

            if seat not in reserved:
                raise Exception("Seat Not Reserved.")

            reserved.remove(seat)
            seats.append(seat)
            seats.sort()

            print("Booking Cancelled.")

        elif choice == 4:

            print("Reserved Seats:", reserved)

        elif choice == 5:

            break

        else:

            print("Invalid Choice.")

    except Exception as e:
        print(e)