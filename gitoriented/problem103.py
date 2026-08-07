products = {
    "Laptop": 70000,
    "Keyboard": 1500,
    "Mouse": 800,
    "Monitor": 18000,
    "Printer": 25000
}

cart = {}

while True:

    try:
        print("\n========== COMPUTER SHOP ==========")
        print("1. View Products")
        print("2. Buy Product")
        print("3. View Bill")
        print("4. Exit")

        choice = int(input("Enter Choice: "))

        if choice == 1:

            for item, price in products.items():
                print(item, ":", price)

        elif choice == 2:

            item = input("Product Name: ")

            if item not in products:
                raise Exception("Product Not Available.")

            qty = int(input("Quantity: "))

            cart[item] = cart.get(item, 0) + qty

            print("Product Added Successfully.")

        elif choice == 3:

            total = 0

            print("\n========== BILL ==========")

            for item, qty in cart.items():

                subtotal = qty * products[item]

                total += subtotal

                print(item, "x", qty, "=", subtotal)

            print("-------------------------")
            print("Grand Total = Rs.", total)

        elif choice == 4:

            print("Thank You For Shopping!")
            break

        else:

            print("Invalid Choice.")

    except Exception as e:
        print(e)