numbers = list(map(int, input("Enter numbers: ").split()))

best_number = numbers[0]
best_count = 0

for number in numbers:
    count = 0

    for i in range(1, number + 1):
        if number % i == 0:
            count += 1

    if count > best_count:
        best_count = count
        best_number = number

print("Number with most divisors:", best_number)
print("Number of divisors:", best_count)