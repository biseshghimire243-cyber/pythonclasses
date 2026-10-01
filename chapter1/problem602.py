numbers = list(map(int, input("Enter numbers: ").split()))

count = 0

for number in numbers:
    digits = str(abs(number))

    has_even = any(int(d) % 2 == 0 for d in digits)
    has_odd = any(int(d) % 2 != 0 for d in digits)

    if has_even and has_odd:
        count += 1

print("Count:", count)