numbers = list(map(int, input("Enter numbers: ").split()))

def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True

total = 0

for i in range(len(numbers)):
    if is_prime(i):
        total += numbers[i]

print("Sum at prime indexes:", total)