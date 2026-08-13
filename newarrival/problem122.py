movies = {
    1: {"name": "Action Movie", "price": 300, "seats": 30},
    2: {"name": "Comedy Movie", "price": 250, "seats": 25},
    3: {"name": "Science Fiction", "price": 350, "seats": 20}
}

bookings = []


def show_movies():

    print("\n========== MOVIES ==========")

    for movie_id, movie in movies.items():

        print(
            movie_id,
            "|",
            movie["name"],
            "| Rs.",
            movie["price"],
            "| Seats:",
            movie["seats"]
        )


def book_ticket():

    movie_id = int(input("Movie ID: "))

    if movie_id not in movies:
        raise Exception("Movie not found.")

    quantity = int(input("Number of tickets: "))

    if quantity <= 0:
        raise Exception("Invalid quantity.")

    if quantity > movies[movie_id]["seats"]:
        raise Exception("Not enough seats.")

    customer = input("Customer Name: ")

    total = quantity * movies[movie_id]["price"]

    movies[movie_id]["seats"] -= quantity

    bookings.append({
        "Customer": customer,
        "Movie": movies[movie_id]["name"],
        "Tickets": quantity,
        "Total": total
    })

    print("Booking successful.")
    print("Total: Rs.", total)


def view_bookings():

    if not bookings:
        print("No bookings.")
        return

    for booking in bookings:

        print("\n-------------------------")
        print("Customer:", booking["Customer"])
        print("Movie:", booking["Movie"])
        print("Tickets:", booking["Tickets"])
        print("Total:", booking["Total"])


while True:

    try:

        print("\n========== MOVIE BOOKING ==========")
        print("1. Show Movies")
        print("2. Book Ticket")
        print("3. View Bookings")
        print("4. Exit")

        choice = int(input("Choice: "))

        if choice == 1:
            show_movies()

        elif choice == 2:
            book_ticket()

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