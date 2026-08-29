age = int(input("Enter age: "))
tickets = int(input("Enter number of tickets: "))

if age < 5:
    price = 0
elif age <= 12:
    price = 150
elif age <= 59:
    price = 250
else:
    price = 180

total = price * tickets

print("Price per ticket:", price)
print("Total amount:", total)