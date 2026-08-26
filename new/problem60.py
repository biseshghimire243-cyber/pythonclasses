tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        if not tasks:
            print("No tasks available")
        else:
            for i, task in enumerate(tasks, 1):
                print(i, ".", task)

    elif choice == "3":
        if tasks:
            number = int(input("Enter task number: "))

            if 1 <= number <= len(tasks):
                removed = tasks.pop(number - 1)
                print("Removed:", removed)
            else:
                print("Invalid task number")
        else:
            print("No tasks available")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")