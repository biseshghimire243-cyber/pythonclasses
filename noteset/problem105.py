books = {}


def add_book():

    book_id = input("Enter Book ID: ")

    if book_id in books:
        raise Exception("Book already exists.")

    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    price = float(input("Enter Price: "))
    quantity = int(input("Enter Quantity: "))

    if price <= 0 or quantity <= 0:
        raise Exception("Price and quantity must be positive.")

    books[book_id] = {
        "Title": title,
        "Author": author,
        "Price": price,
        "Quantity": quantity
    }

    print("Book added successfully.")


def view_books():

    if len(books) == 0:
        print("No books available.")
        return

    print("\n========== BOOK LIST ==========")

    for book_id, book in books.items():

        print("----------------------------")
        print("ID:", book_id)
        print("Title:", book["Title"])
        print("Author:", book["Author"])
        print("Price:", book["Price"])
        print("Quantity:", book["Quantity"])


def search_book():

    keyword = input("Enter book title to search: ").lower()

    found = False

    for book_id, book in books.items():

        if keyword in book["Title"].lower():

            print("\nBook Found")
            print("ID:", book_id)
            print("Title:", book["Title"])
            print("Author:", book["Author"])
            print("Price:", book["Price"])
            print("Quantity:", book["Quantity"])

            found = True

    if not found:
        print("Book not found.")


def buy_book():

    book_id = input("Enter Book ID: ")

    if book_id not in books:
        raise Exception("Book not found.")

    quantity = int(input("Enter quantity: "))

    if quantity <= 0:
        raise Exception("Invalid quantity.")

    if quantity > books[book_id]["Quantity"]:
        raise Exception("Not enough books in stock.")

    price = books[book_id]["Price"]

    total = price * quantity

    books[book_id]["Quantity"] -= quantity

    print("\n========== BILL ==========")
    print("Book:", books[book_id]["Title"])
    print("Quantity:", quantity)
    print("Price:", price)
    print("Total: Rs.", total)


def remove_book():

    book_id = input("Enter Book ID: ")

    if book_id not in books:
        raise Exception("Book not found.")

    del books[book_id]

    print("Book removed successfully.")


while True:

    try:

        print("\n========== BOOK STORE ==========")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Buy Book")
        print("5. Remove Book")
        print("6. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            add_book()

        elif choice == 2:
            view_books()

        elif choice == 3:
            search_book()

        elif choice == 4:
            buy_book()

        elif choice == 5:
            remove_book()

        elif choice == 6:
            print("Thank you.")
            break

        else:
            print("Invalid choice.")

    except ValueError:

        print("Please enter valid input.")

    except Exception as e:

        print("Error:", e)