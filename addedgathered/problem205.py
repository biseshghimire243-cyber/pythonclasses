numbers = list(map(int, input("Enter numbers: ").split()))

positive_numbers = []

for num in numbers:
    if num >= 0:
        positive_numbers.append(num)

print("Original list:", numbers)
print("After removing negative numbers:", positive_numbers)