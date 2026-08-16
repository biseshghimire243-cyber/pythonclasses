class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def issue(self):

        if not self.available:
            print("Book is already issued.")
            return

        self.available = False
        print("Book issued successfully.")

    def return_book(self):

        self.available = True
        print("Book returned successfully.")

    def display(self):

        status = "Available" if self.available else "Issued"

        print(
            self.title,
            "|",
            self.author,
            "|",
            status
        )


books = []

books.append(Book("Python Programming", "John"))
books.append(Book("Database Systems", "James"))
books.append(Book("Web Development", "Robert"))

while True:

    print("\n1. View Books")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Exit")

    choice = input("Choice: ")

    if choice == "1":

        for book in books:
            book.display()

    elif choice == "2":

        title = input("Book title: ")

        for book in books:

            if book.title.lower() == title.lower():
                book.issue()
                break

        else:
            print("Book not found.")

    elif choice == "3":

        title = input("Book title: ")

        for book in books:

            if book.title.lower() == title.lower():
                book.return_book()
                break

        else:
            print("Book not found.")

    elif choice == "4":
        break

    else:
        print("Invalid choice.")