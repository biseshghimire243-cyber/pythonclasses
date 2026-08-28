inventory = {
    "Laptop": 10,
    "Mouse": 25,
    "Keyboard": 15,
    "Monitor": 8
}

item = input("Enter item name: ")

if item in inventory:
    print("Available quantity:", inventory[item])

    quantity = int(input("Enter quantity to sell: "))

    if quantity <= inventory[item]:
        inventory[item] -= quantity
        print("Sale successful!")
        print("Remaining:", inventory[item])
    else:
        print("Not enough stock")

else:
    print("Item not found")