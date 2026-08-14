import json
import os


class Library:

    def __init__(self, filename="library.json"):
        self.filename = filename
        self.books = []
        self.load_books()

    def load_books(self):

        if os.path.exists(self.filename):

            with open(self.filename, "r") as file:

                self.books = json.load(file)

    def save_books(self):

        with open(self.filename, "w") as file:

            json.dump(
                self.books,
                file,
                indent=4
            )

    def add_book(self):

        book_id = input("Book ID: ")
        title = input("Book Title: ")
        author = input("Author: ")

        book = {
            "id": book_id,
            "title": title,
            "author": author
        }

        self.books.append(book)

        self.save_books()

        print("Book saved.")

    def view_books(self):

        if not self.books:

            print("No books available.")
            return

        print("\n========== LIBRARY ==========")

        for book in self.books:

            print(
                book["id"],
                "|",
                book["title"],
                "|",
                book["author"]
            )


library = Library()

while True:

    print("\n========== LIBRARY SYSTEM ==========")
    print("1. Add Book")
    print("2. View Books")
    print("3. Exit")

    choice = input("Choice: ")

    if choice == "1":

        library.add_book()

    elif choice == "2":

        library.view_books()

    elif choice == "3":

        break

    else:

        print("Invalid choice.")