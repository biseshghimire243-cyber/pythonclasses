menu = {
    1: {"name": "Burger", "price": 250},
    2: {"name": "Pizza", "price": 500},
    3: {"name": "Momo", "price": 180},
    4: {"name": "Chowmein", "price": 150},
    5: {"name": "Coke", "price": 100}
}

order = {}


def show_menu():

    print("\n========== MENU ==========")

    for item_id, item in menu.items():
        print(item_id, item["name"], "- Rs.", item["price"])


def add_order():

    item_id = int(input("Enter item ID: "))

    if item_id not in menu:
        raise Exception("Item not found.")

    quantity = int(input("Quantity: "))

    if quantity <= 0:
        raise Exception("Invalid quantity.")

    order[item_id] = order.get(item_id, 0) + quantity

    print("Item added.")


def show_bill():

    if not order:
        print("Order is empty.")
        return

    total = 0

    print("\n========== BILL ==========")

    for item_id, quantity in order.items():

        item = menu[item_id]

        subtotal = item["price"] * quantity

        total += subtotal

        print(
            item["name"],
            "x",
            quantity,
            "=",
            subtotal
        )

    tax = total * 0.13
    grand_total = total + tax

    print("--------------------------")
    print("Subtotal:", total)
    print("Tax:", tax)
    print("Grand Total:", grand_total)


while True:

    try:

        print("\n========== RESTAURANT ==========")
        print("1. Show Menu")
        print("2. Add Order")
        print("3. View Bill")
        print("4. Exit")

        choice = int(input("Choice: "))

        if choice == 1:
            show_menu()

        elif choice == 2:
            add_order()

        elif choice == 3:
            show_bill()

        elif choice == 4:
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Enter valid input.")

    except Exception as e:
        print("Error:", e)