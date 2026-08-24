number = int(input("Enter a number: "))

total = 0

for i in range(1, 11):
    result = number * i
    total += result

print("Sum of multiplication table:", total)