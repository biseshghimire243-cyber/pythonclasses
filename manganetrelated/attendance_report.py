limit = int(input("Enter limit: "))

total = 0

for number in range(2, limit + 1, 2):
    total += number

print("Sum of even numbers:", total)