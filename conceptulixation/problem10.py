inventory = {
    "Laptop": 5,
    "Phone": 10,
    "Keyboard": 15,
    "Mouse": 20
}

print("===== INVENTORY =====")

for item, quantity in inventory.items():
    print(item, ":", quantity)

item = input("Enter item to check: ")

if item in inventory:
    print("Available quantity:", inventory[item])
else:
    print("Item not found.")