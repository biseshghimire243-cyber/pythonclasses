inventory = {}


def add_product():

    product_id = input("Product ID: ")

    name = input("Product Name: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))

    inventory[product_id] = {
        "Name": name,
        "Price": price,
        "Quantity": quantity
    }

    print("Product added.")


def sell_product():

    product_id = input("Product ID: ")

    if product_id not in inventory:
        raise Exception("Product not found.")

    quantity = int(input("Quantity sold: "))

    if quantity > inventory[product_id]["Quantity"]:
        raise Exception("Insufficient stock.")

    inventory[product_id]["Quantity"] -= quantity

    total = quantity * inventory[product_id]["Price"]

    print("Sale completed.")
    print("Total: Rs.", total)


def restock():

    product_id = input("Product ID: ")

    if product_id not in inventory:
        raise Exception("Product not found.")

    quantity = int(input("Quantity to add: "))

    inventory[product_id]["Quantity"] += quantity

    print("Stock updated.")


def view_inventory():

    print("\n========== INVENTORY ==========")

    for product_id, product in inventory.items():

        print("--------------------------")
        print("ID:", product_id)
        print("Name:", product["Name"])
        print("Price:", product["Price"])
        print("Stock:", product["Quantity"])


while True:

    try:

        print("\n========== INVENTORY SYSTEM ==========")
        print("1. Add Product")
        print("2. Sell Product")
        print("3. Restock")
        print("4. View Inventory")
        print("5. Exit")

        choice = int(input("Choice: "))

        if choice == 1:
            add_product()

        elif choice == 2:
            sell_product()

        elif choice == 3:
            restock()

        elif choice == 4:
            view_inventory()

        elif choice == 5:
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Enter valid input.")

    except Exception as e:
        print("Error:", e)