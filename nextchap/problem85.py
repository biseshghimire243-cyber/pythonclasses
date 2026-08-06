movies = {
    "Avengers": 50,
    "Avatar": 40,
    "Spider-Man": 30
}

bookings = {}

while True:

    try:

        print("\n========== MOVIE BOOKING ==========")
        print("1. View Movies")
        print("2. Book Ticket")
        print("3. Cancel Ticket")
        print("4. View Bookings")
        print("5. Exit")

        choice = int(input("Enter Choice: "))

        if choice == 1:

            for movie, seats in movies.items():
                print(movie, "-", seats, "Seats")

        elif choice == 2:

            movie = input("Movie Name: ")

            if movie not in movies:
                raise Exception("Movie Not Found.")

            seats = int(input("Number of Seats: "))

            if seats > movies[movie]:
                raise Exception("Not Enough Seats.")

            movies[movie] -= seats
            bookings[movie] = bookings.get(movie, 0) + seats

            print("Ticket Booked Successfully.")

        elif choice == 3:

            movie = input("Movie Name: ")

            if movie not in bookings:
                raise Exception("Booking Not Found.")

            seats = bookings[movie]

            movies[movie] += seats

            del bookings[movie]

            print("Booking Cancelled.")

        elif choice == 4:

            print(bookings)

        elif choice == 5:
            break

        else:
            print("Invalid Choice.")

    except Exception as e:
        print(e)