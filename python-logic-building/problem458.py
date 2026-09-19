numbers = list(map(int, input("Enter numbers: ").split()))

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

total = 0

for number in numbers:
    if is_prime(number):
        total += number

print("Sum of prime numbers:", total)