numbers = list(map(int, input("Enter numbers: ").split()))

best_number = None
largest_difference = -1

for number in numbers:
    odd = 0
    even = 0

    for digit in str(abs(number)):
        if int(digit) % 2 == 0:
            even += 1
        else:
            odd += 1

    difference = abs(odd - even)

    if difference > largest_difference:
        largest_difference = difference
        best_number = number

print("Number:", best_number)
print("Largest odd-even digit difference:", largest_difference)