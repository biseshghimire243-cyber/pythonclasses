products = {
    "Rice": 80,
    "Sugar": 100,
    "Milk": 60,
    "Soap": 50
}

cart = {}

while True:

    try:

        print("\n========== SUPERMARKET ==========")
        print("1. View Products")
        print("2. Buy Product")
        print("3. View Bill")
        print("4. Exit")

        choice = int(input("Choice: "))

        if choice == 1:

            for item, price in products.items():
                print(item, "-", price)

        elif choice == 2:

            item = input("Product Name: ")

            if item not in products:
                raise Exception("Product Not Found.")

            qty = int(input("Quantity: "))

            cart[item] = cart.get(item, 0) + qty

            print("Added Successfully.")

        elif choice == 3:

            total = 0

            print("\n===== BILL =====")

            for item, qty in cart.items():

                subtotal = products[item] * qty

                total += subtotal

                print(item, qty, subtotal)

            print("-------------------")
            print("Total =", total)

        elif choice == 4:
            break

    except Exception as e:
        print(e)