class Vehicle:

    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print("Vehicle starting.")


class Car(Vehicle):

    def start(self):
        print(self.brand, "car starts with a key.")


class Bike(Vehicle):

    def start(self):
        print(self.brand, "bike starts with a button.")


class Bus(Vehicle):

    def start(self):
        print(self.brand, "bus starts with an engine.")


vehicles = [
    Car("Toyota"),
    Bike("Yamaha"),
    Bus("Tata")
]

for vehicle in vehicles:

    vehicle.start()