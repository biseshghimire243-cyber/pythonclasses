initial = float(input("Enter initial savings: "))
monthly = float(input("Enter monthly saving: "))
months = int(input("Enter number of months: "))

total = initial

for month in range(1, months + 1):
    total += monthly

print("Total savings:", total)
print("Total added:", total - initial)