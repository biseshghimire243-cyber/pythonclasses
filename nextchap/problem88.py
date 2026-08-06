menu = {
    "Pizza": 450,
    "Burger": 250,
    "Momo": 180,
    "Chowmein": 200,
    "Coffee": 120
}

cart = {}

while True:

    try:

        print("\n========== FOOD ORDERING SYSTEM ==========")
        print("1. View Menu")
        print("2. Order Food")
        print("3. View Cart")
        print("4. Remove Food")
        print("5. Checkout")
        print("6. Exit")

        choice = int(input("Enter Choice: "))

        if choice == 1:

            print("\n------ MENU ------")

            for item, price in menu.items():
                print(f"{item} : Rs. {price}")

        elif choice == 2:

            item = input("Food Name: ")

            if item not in menu:
                raise Exception("Food Not Available.")

            qty = int(input("Quantity: "))

            if qty <= 0:
                raise Exception("Quantity must be greater than zero.")

            cart[item] = cart.get(item, 0) + qty

            print("Food Added Successfully.")

        elif choice == 3:

            total = 0

            print("\n------ CART ------")

            if len(cart) == 0:
                print("Cart is Empty.")

            else:

                for item, qty in cart.items():

                    subtotal = menu[item] * qty

                    total += subtotal

                    print(item, qty, "=", subtotal)

                print("------------------")
                print("Total = Rs.", total)

        elif choice == 4:

            item = input("Food Name: ")

            if item not in cart:
                raise Exception("Food Not Found.")

            del cart[item]

            print("Item Removed.")

        elif choice == 5:

            total = 0

            for item, qty in cart.items():
                total += menu[item] * qty

            print("\nTotal Bill = Rs.", total)
            print("Order Successful.")
            cart.clear()

        elif choice == 6:

            print("Thank You.")
            break

        else:

            print("Invalid Choice.")

    except Exception as e:
        print(e)