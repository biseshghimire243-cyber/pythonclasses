class Inventory:

    def __init__(self):

        self.products = {}

    def add_product(self):

        name = input("Product Name: ")
        quantity = int(input("Quantity: "))
        price = float(input("Price: "))

        self.products[name] = {
            "quantity": quantity,
            "price": price
        }

        print("Product added.")

    def sell_product(self):

        name = input("Product Name: ")

        if name not in self.products:

            print("Product not found.")
            return

        quantity = int(
            input("Quantity to sell: ")
        )

        product = self.products[name]

        if quantity > product["quantity"]:

            print("Not enough stock.")
            return

        product["quantity"] -= quantity

        total = quantity * product["price"]

        print("Sale completed.")
        print("Total: Rs.", total)

    def display(self):

        print("\n========== INVENTORY ==========")

        for name, product in self.products.items():

            print(
                name,
                "| Quantity:",
                product["quantity"],
                "| Price:",
                product["price"]
            )


inventory = Inventory()

while True:

    print("\n1. Add Product")
    print("2. Sell Product")
    print("3. View Inventory")
    print("4. Exit")

    choice = input("Choice: ")

    if choice == "1":

        inventory.add_product()

    elif choice == "2":

        inventory.sell_product()

    elif choice == "3":

        inventory.display()

    elif choice == "4":

        break

    else:

        print("Invalid choice.")