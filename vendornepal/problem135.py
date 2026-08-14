class Vehicle:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print("Vehicle is starting.")


class Car(Vehicle):

    def start(self):
        print(self.brand, self.model, "starts with a key.")


class ElectricCar(Vehicle):

    def start(self):
        print(self.brand, self.model, "starts silently using electricity.")


class Motorcycle(Vehicle):

    def start(self):
        print(self.brand, self.model, "starts with a motorcycle engine.")


vehicles = [
    Car("Toyota", "Corolla"),
    ElectricCar("Tesla", "Model 3"),
    Motorcycle("Yamaha", "R15")
]


print("========== VEHICLES ==========")

for vehicle in vehicles:

    print(
        "\nBrand:",
        vehicle.brand,
        "\nModel:",
        vehicle.model
    )

    vehicle.start()