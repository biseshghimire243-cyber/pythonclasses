distance = float(input("Enter distance traveled (km): "))
mileage = float(input("Enter vehicle mileage (km/l): "))
fuel_price = float(input("Enter fuel price per liter: "))

fuel_used = distance / mileage
total_cost = fuel_used * fuel_price

print("Fuel used:", round(fuel_used, 2), "liters")
print("Total fuel cost:", round(total_cost, 2))