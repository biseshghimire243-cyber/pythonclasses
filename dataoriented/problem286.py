text = input("Enter a string: ")

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

result = ""

for i, char in enumerate(text, start=1):
    if is_prime(i):
        result += char

print("Characters at prime positions:", result)