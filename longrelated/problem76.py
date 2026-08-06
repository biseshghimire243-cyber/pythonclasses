library = []

while True:
    try:
        print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Delete Book")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            book = input("Enter Book Name: ")

            if book in library:
                raise Exception("Book already exists.")

            library.append(book)
            print("Book Added Successfully.")

        elif choice == 2:
            if len(library) == 0:
                print("No books available.")
            else:
                print("\nAvailable Books")
                for i, book in enumerate(library, start=1):
                    print(i, ".", book)

        elif choice == 3:
            book = input("Enter Book Name: ")

            if book in library:
                print("Book Found.")
            else:
                raise Exception("Book Not Found.")

        elif choice == 4:
            book = input("Enter Book Name to Issue: ")

            if book not in library:
                raise Exception("Book Not Available.")

            library.remove(book)
            print("Book Issued Successfully.")

        elif choice == 5:
            book = input("Enter Returned Book Name: ")
            library.append(book)
            print("Book Returned Successfully.")

        elif choice == 6:
            book = input("Enter Book Name to Delete: ")

            if book not in library:
                raise Exception("Book Not Found.")

            library.remove(book)
            print("Book Deleted Successfully.")

        elif choice == 7:
            print("Thank You.")
            break

        else:
            print("Invalid Choice.")

    except ValueError:
        print("Please enter a valid number.")

    except Exception as e:
        print(e)