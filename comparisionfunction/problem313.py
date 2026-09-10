number = input("Enter a number: ")

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

rotations = []
current = number

for _ in range(len(number)):
    rotations.append(int(current))
    current = current[1:] + current[0]

if all(is_prime(n) for n in rotations):
    print("Circular prime")
else:
    print("Not a circular prime")