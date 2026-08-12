products = {
    101: {
        "Name": "Laptop",
        "Price": 75000,
        "Stock": 5
    },
    102: {
        "Name": "Phone",
        "Price": 35000,
        "Stock": 10
    },
    103: {
        "Name": "Headphones",
        "Price": 2500,
        "Stock": 15
    },
    104: {
        "Name": "Keyboard",
        "Price": 1800,
        "Stock": 20
    }
}

cart = {}


def view_products():

    print("\n========== PRODUCTS ==========")

    for product_id, product in products.items():

        print("-----------------------------")
        print("ID:", product_id)
        print("Name:", product["Name"])
        print("Price:", product["Price"])
        print("Stock:", product["Stock"])


def search_product():

    keyword = input("Search Product: ").lower()

    found = False

    for product_id, product in products.items():

        if keyword in product["Name"].lower():

            print("\nProduct Found")
            print("ID:", product_id)
            print("Name:", product["Name"])
            print("Price:", product["Price"])
            print("Stock:", product["Stock"])

            found = True

    if not found:
        print("Product not found.")


def add_to_cart():

    product_id = int(input("Enter Product ID: "))

    if product_id not in products:
        raise Exception("Product not found.")

    quantity = int(input("Enter Quantity: "))

    if quantity <= 0:
        raise Exception("Invalid quantity.")

    current_quantity = cart.get(product_id, 0)

    if current_quantity + quantity > products[product_id]["Stock"]:
        raise Exception("Not enough stock.")

    cart[product_id] = current_quantity + quantity

    print("Product added to cart.")


def remove_from_cart():

    product_id = int(input("Enter Product ID: "))

    if product_id not in cart:
        raise Exception("Product is not in cart.")

    del cart[product_id]

    print("Product removed from cart.")


def view_cart():

    if len(cart) == 0:
        print("Your cart is empty.")
        return

    total = 0

    print("\n========== YOUR CART ==========")

    for product_id, quantity in cart.items():

        product = products[product_id]

        subtotal = product["Price"] * quantity

        total += subtotal

        print(
            product["Name"],
            "x",
            quantity,
            "=",
            subtotal
        )

    print("-----------------------------")
    print("Total:", total)


def checkout():

    if len(cart) == 0:
        raise Exception("Cart is empty.")

    total = 0

    for product_id, quantity in cart.items():

        product = products[product_id]

        total += product["Price"] * quantity

    discount = 0

    if total >= 100000:
        discount = total * 0.10

    elif total >= 50000:
        discount = total * 0.05

    final_amount = total - discount

    for product_id, quantity in cart.items():

        products[product_id]["Stock"] -= quantity

    print("\n========== FINAL BILL ==========")
    print("Total Amount:", total)
    print("Discount:", discount)
    print("Final Amount:", final_amount)

    cart.clear()

    print("Order placed successfully!")


while True:

    try:

        print("\n========== E-COMMERCE SYSTEM ==========")
        print("1. View Products")
        print("2. Search Product")
        print("3. Add to Cart")
        print("4. Remove from Cart")
        print("5. View Cart")
        print("6. Checkout")
        print("7. Exit")

        choice = int(input("Enter Choice: "))

        if choice == 1:
            view_products()

        elif choice == 2:
            search_product()

        elif choice == 3:
            add_to_cart()

        elif choice == 4:
            remove_from_cart()

        elif choice == 5:
            view_cart()

        elif choice == 6:
            checkout()

        elif choice == 7:
            print("Thank you for shopping.")
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Please enter valid input.")

    except Exception as e:
        print("Error:", e)