numbers = list(map(int, input("Enter numbers: ").split()))

found = None

for number in numbers:
    digit_sum = sum(int(digit) for digit in str(abs(number)))
    text = str(digit_sum)

    if text == text[::-1]:
        found = number
        break

if found is not None:
    print("First number with palindromic digit sum:", found)
else:
    print("No matching number found.")