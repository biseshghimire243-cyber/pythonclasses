import json
import os


class Library:

    def __init__(self):

        self.filename = "library.json"
        self.books = self.load()

    def load(self):

        if not os.path.exists(self.filename):
            return []

        with open(self.filename, "r") as file:

            return json.load(file)

    def save(self):

        with open(self.filename, "w") as file:

            json.dump(
                self.books,
                file,
                indent=4
            )

    def add_book(self):

        book = {

            "title": input("Book Title: "),
            "author": input("Author: "),
            "year": input("Publication Year: ")
        }

        self.books.append(book)

        self.save()

        print("Book saved.")

    def search_book(self):

        title = input("Book title: ")

        for book in self.books:

            if book["title"].lower() == title.lower():

                print("\nBook Found")
                print("Title:", book["title"])
                print("Author:", book["author"])
                print("Year:", book["year"])

                return

        print("Book not found.")

    def display(self):

        print("\n========== LIBRARY ==========")

        for book in self.books:

            print(
                book["title"],
                "|",
                book["author"],
                "|",
                book["year"]
            )


library = Library()

while True:

    print("\n1. Add Book")
    print("2. Search Book")
    print("3. View Books")
    print("4. Exit")

    choice = input("Choice: ")

    if choice == "1":

        library.add_book()

    elif choice == "2":

        library.search_book()

    elif choice == "3":

        library.display()

    elif choice == "4":

        break

    else:

        print("Invalid choice.")