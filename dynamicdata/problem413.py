numbers = list(map(int, input("Enter numbers: ").split()))

frequency = {}

for number in numbers:
    first_digit = str(abs(number))[0]
    frequency[first_digit] = frequency.get(first_digit, 0) + 1

most_common = max(frequency, key=frequency.get)

print("Most common first digit:", most_common)
print("Occurrences:", frequency[most_common])