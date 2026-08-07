medicines = {}

while True:

    try:
        print("\n========== PHARMACY MANAGEMENT ==========")
        print("1. Add Medicine")
        print("2. View Medicines")
        print("3. Sell Medicine")
        print("4. Search Medicine")
        print("5. Exit")

        choice = int(input("Enter Choice: "))

        if choice == 1:

            medicine = input("Medicine Name: ")
            quantity = int(input("Quantity: "))
            price = float(input("Price: "))

            medicines[medicine] = {
                "Quantity": quantity,
                "Price": price
            }

            print("Medicine Added Successfully.")

        elif choice == 2:

            if len(medicines) == 0:
                print("No Medicines Available.")

            else:
                for medicine, data in medicines.items():
                    print("-----------------------")
                    print("Medicine:", medicine)
                    print("Quantity:", data["Quantity"])
                    print("Price   :", data["Price"])

        elif choice == 3:

            medicine = input("Medicine Name: ")

            if medicine not in medicines:
                raise Exception("Medicine Not Found.")

            qty = int(input("Quantity to Sell: "))

            if qty > medicines[medicine]["Quantity"]:
                raise Exception("Insufficient Stock.")

            medicines[medicine]["Quantity"] -= qty

            total = qty * medicines[medicine]["Price"]

            print("Total Bill = Rs.", total)

        elif choice == 4:

            medicine = input("Medicine Name: ")

            if medicine not in medicines:
                raise Exception("Medicine Not Found.")

            print(medicines[medicine])

        elif choice == 5:
            break

        else:
            print("Invalid Choice.")

    except Exception as e:
        print(e)