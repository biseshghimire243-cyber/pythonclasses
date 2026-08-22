start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print("Prime numbers:")

for number in range(start, end + 1):
    if number < 2:
        continue

    prime = True

    for i in range(2, number):
        if number % i == 0:
            prime = False
            break

    if prime:
        print(number, end=" ")