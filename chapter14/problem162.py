class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cart:

    def __init__(self):
        self.products = []

    def add_product(self, product):

        self.products.append(product)

        print(product.name, "added to cart.")

    def remove_product(self, name):

        for product in self.products:

            if product.name.lower() == name.lower():

                self.products.remove(product)

                print("Product removed.")
                return

        print("Product not found.")

    def total(self):

        return sum(product.price for product in self.products)

    def display(self):

        print("\n========== CART ==========")

        for product in self.products:

            print(
                product.name,
                "- Rs.",
                product.price
            )

        print("Total: Rs.", self.total())


cart = Cart()

cart.add_product(Product("Laptop", 75000))
cart.add_product(Product("Mouse", 1200))
cart.add_product(Product("Keyboard", 2500))

cart.display()

cart.remove_product("Mouse")

cart.display()