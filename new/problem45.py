cart = {
    "Laptop": 80000,
    "Mouse": 1500,
    "Keyboard": 3000,
    "Headphone": 2500
}

total = 0

print("===== SHOPPING CART =====")

for item, price in cart.items():
    print(item, ":", price)
    total += price

print("-------------------------")
print("Total Amount:", total)