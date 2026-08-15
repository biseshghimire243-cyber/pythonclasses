class FoodItem:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:

    def __init__(self, customer):
        self.customer = customer
        self.items = []
        self.status = "Preparing"

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):

        total = 0

        for item in self.items:
            total += item.price

        return total

    def update_status(self, status):

        valid = [
            "Preparing",
            "Out for Delivery",
            "Delivered"
        ]

        if status not in valid:
            raise ValueError("Invalid status.")

        self.status = status

    def show_order(self):

        print("\n========== ORDER ==========")
        print("Customer:", self.customer)

        for item in self.items:
            print(
                item.name,
                "- Rs.",
                item.price
            )

        print("Total: Rs.", self.calculate_total())
        print("Status:", self.status)


pizza = FoodItem("Pizza", 500)
burger = FoodItem("Burger", 250)
momo = FoodItem("Momo", 180)

order = Order("Bishesh")

order.add_item(pizza)
order.add_item(burger)
order.add_item(momo)

order.show_order()

order.update_status("Out for Delivery")

order.show_order()