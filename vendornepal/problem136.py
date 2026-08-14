class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class ShoppingCart:

    def __init__(self):
        self.products = []

    def add_product(self, product):

        self.products.append(product)
        print(product.name, "added to cart.")

    def remove_product(self, name):

        for product in self.products:

            if product.name.lower() == name.lower():

                self.products.remove(product)

                print(product.name, "removed.")
                return

        print("Product not found.")

    def show_cart(self):

        if not self.products:
            print("Cart is empty.")
            return

        total = 0

        print("\n========== SHOPPING CART ==========")

        for product in self.products:

            print(
                product.name,
                "- Rs.",
                product.price
            )

            total += product.price

        print("----------------------------")
        print("Total: Rs.", total)


laptop = Product("Laptop", 75000)
mouse = Product("Mouse", 1200)
keyboard = Product("Keyboard", 2500)

cart = ShoppingCart()

cart.add_product(laptop)
cart.add_product(mouse)
cart.add_product(keyboard)

cart.show_cart()

cart.remove_product("Mouse")

cart.show_cart()