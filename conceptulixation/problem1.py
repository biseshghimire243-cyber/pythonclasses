age = int(input("Enter your age: "))
tickets = int(input("Enter number of tickets: "))

if age < 12:
    price = 150
elif age >= 60:
    price = 200
else:
    price = 300

total = price * tickets

print("Ticket Price:", price)
print("Total Amount:", total)