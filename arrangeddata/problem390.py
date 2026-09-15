number = input("Enter a number: ")

frequency = {}

for digit in number:
    frequency[digit] = frequency.get(digit, 0) + 1

for digit, count in frequency.items():
    print(digit, ":", count)