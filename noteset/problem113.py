products = []

customer_name = ""
customer_phone = ""


def add_customer():

    global customer_name
    global customer_phone

    customer_name = input("Customer Name: ")
    customer_phone = input("Customer Phone: ")

    print("Customer information saved.")


def add_product():

    name = input("Product Name: ")
    price = float(input("Product Price: "))
    quantity = int(input("Quantity: "))

    if price <= 0 or quantity <= 0:
        raise Exception("Price and quantity must be positive.")

    products.append({
        "Name": name,
        "Price": price,
        "Quantity": quantity
    })

    print("Product added to invoice.")


def generate_invoice():

    if customer_name == "":
        raise Exception("Please add customer information first.")

    if len(products) == 0:
        raise Exception("Invoice has no products.")

    subtotal = 0

    print("\n")
    print("=" * 45)
    print("             INVOICE")
    print("=" * 45)

    print("Customer:", customer_name)
    print("Phone:", customer_phone)

    print("-" * 45)

    for product in products:

        total = product["Price"] * product["Quantity"]

        subtotal += total

        print(
            product["Name"],
            "x",
            product["Quantity"],
            "=",
            total
        )

    discount = 0

    if subtotal >= 100000:
        discount = subtotal * 0.10

    elif subtotal >= 50000:
        discount = subtotal * 0.05

    after_discount = subtotal - discount

    tax = after_discount * 0.13

    grand_total = after_discount + tax

    print("-" * 45)
    print("Subtotal:", subtotal)
    print("Discount:", discount)
    print("Tax (13%):", tax)
    print("Grand Total:", grand_total)
    print("=" * 45)

    print("Thank you for shopping!")


while True:

    try:

        print("\n========== INVOICE GENERATOR ==========")
        print("1. Add Customer")
        print("2. Add Product")
        print("3. Generate Invoice")
        print("4. Exit")

        choice = int(input("Enter Choice: "))

        if choice == 1:
            add_customer()

        elif choice == 2:
            add_product()

        elif choice == 3:
            generate_invoice()

        elif choice == 4:
            print("Program Closed.")
            break

        else:
            print("Invalid choice.")

    except ValueError:

        print("Please enter valid numeric input.")

    except Exception as e:

        print("Error:", e)