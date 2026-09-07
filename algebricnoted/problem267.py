number = int(input("Enter a number: "))


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


distance = 0

while True:
    lower = number - distance
    upper = number + distance

    if is_prime(lower):
        print("Nearest prime:", lower)
        break

    if is_prime(upper):
        print("Nearest prime:", upper)
        break

    distance += 1