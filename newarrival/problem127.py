books = {}


def issue_book():

    book_id = input("Book ID: ")
    title = input("Book Title: ")
    student = input("Student Name: ")
    days = int(input("Days kept: "))

    books[book_id] = {
        "Title": title,
        "Student": student,
        "Days": days
    }

    print("Book issued.")


def calculate_fine():

    book_id = input("Book ID: ")

    if book_id not in books:
        raise Exception("Book not found.")

    days = books[book_id]["Days"]

    free_days = 7

    if days <= free_days:
        fine = 0

    else:
        late_days = days - free_days
        fine = late_days * 10

    print("Book:", books[book_id]["Title"])
    print("Days:", days)
    print("Fine: Rs.", fine)


def view_books():

    for book_id, book in books.items():

        print("\nID:", book_id)
        print("Title:", book["Title"])
        print("Student:", book["Student"])
        print("Days:", book["Days"])


while True:

    try:

        print("\n========== LIBRARY FINE SYSTEM ==========")
        print("1. Issue Book")
        print("2. Calculate Fine")
        print("3. View Books")
        print("4. Exit")

        choice = int(input("Choice: "))

        if choice == 1:
            issue_book()

        elif choice == 2:
            calculate_fine()

        elif choice == 3:
            view_books()

        elif choice == 4:
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Enter valid input.")

    except Exception as e:
        print("Error:", e)