cart = {}
total = 0

while True:

    try:

        print("\n===== SHOPPING CART =====")
        print("1. Add Product")
        print("2. View Cart")
        print("3. Checkout")
        print("4. Exit")

        choice = int(input("Enter Choice: "))

        if choice == 1:

            product = input("Product Name: ")
            price = float(input("Price: "))
            qty = int(input("Quantity: "))

            cart[product] = {
                "Price": price,
                "Quantity": qty
            }

            print("Product Added.")

        elif choice == 2:

            total = 0

            for product, data in cart.items():

                subtotal = data["Price"] * data["Quantity"]

                total += subtotal

                print(product, "-", subtotal)

            print("Total = Rs.", total)

        elif choice == 3:

            print("Final Bill = Rs.", total)
            print("Thank You For Shopping")
            break

        elif choice == 4:
            break

        else:
            print("Invalid Choice")

    except Exception as e:
        print(e)