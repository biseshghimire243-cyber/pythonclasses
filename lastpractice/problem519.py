numbers = list(map(int, input("Enter numbers: ").split()))

count = 0

for number in numbers:
    odd = 0
    even = 0

    for digit in str(abs(number)):
        if int(digit) % 2 == 0:
            even += 1
        else:
            odd += 1

    if odd > even:
        count += 1

print("Numbers with more odd digits:", count)