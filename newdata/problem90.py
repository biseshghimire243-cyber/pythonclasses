sales = {
    "Monday": 4500,
    "Tuesday": 6200,
    "Wednesday": 3800,
    "Thursday": 7200,
    "Friday": 5600,
    "Saturday": 8100,
    "Sunday": 4900
}

total = sum(sales.values())
average = total / len(sales)

best_day = max(sales, key=sales.get)
lowest_day = min(sales, key=sales.get)

print("===== SALES REPORT =====")

for day, amount in sales.items():
    print(day, ":", amount)

print("\nTotal Sales:", total)
print("Average Sales:", round(average, 2))
print("Best Sales Day:", best_day)
print("Highest Sales:", sales[best_day])
print("Lowest Sales Day:", lowest_day)
print("Lowest Sales:", sales[lowest_day])