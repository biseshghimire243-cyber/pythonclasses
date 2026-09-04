queue = []

while True:
    print("\n1. Add")
    print("2. Remove")
    print("3. Display")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        item = input("Enter item: ")
        queue.append(item)
        print("Item added.")

    elif choice == "2":
        if queue:
            print("Removed:", queue.pop(0))
        else:
            print("Queue is empty.")

    elif choice == "3":
        print("Queue:", queue)

    elif choice == "4":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")