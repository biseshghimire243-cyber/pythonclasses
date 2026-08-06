inventory = {}

while True:

    try:

        print("\n========== INVENTORY MANAGEMENT ==========")
        print("1. Add Product")
        print("2. View Inventory")
        print("3. Search Product")
        print("4. Update Quantity")
        print("5. Delete Product")
        print("6. Exit")

        choice = int(input("Enter Choice: "))

        if choice == 1:

            product = input("Product Name: ")

            if product in inventory:
                raise Exception("Product Already Exists.")

            quantity = int(input("Quantity: "))

            inventory[product] = quantity

            print("Product Added Successfully.")

        elif choice == 2:

            if len(inventory) == 0:
                print("Inventory Empty.")

            else:

                for product, quantity in inventory.items():

                    print(product, ":", quantity)

        elif choice == 3:

            product = input("Product Name: ")

            if product not in inventory:
                raise Exception("Product Not Found.")

            print(product, "Quantity =", inventory[product])

        elif choice == 4:

            product = input("Product Name: ")

            if product not in inventory:
                raise Exception("Product Not Found.")

            inventory[product] = int(input("New Quantity: "))

            print("Updated Successfully.")

        elif choice == 5:

            product = input("Product Name: ")

            if product not in inventory:
                raise Exception("Product Not Found.")

            del inventory[product]

            print("Deleted Successfully.")

        elif choice == 6:

            print("Program Closed.")
            break

        else:

            print("Invalid Choice.")

    except Exception as e:
        print(e)