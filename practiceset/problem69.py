try:
    book_id = input("Enter Book ID: ")

    if not book_id.startswith("BK"):
        raise Exception("Book ID must start with 'BK'.")

    print("Book ID:", book_id)

except Exception as e:
    print(e)