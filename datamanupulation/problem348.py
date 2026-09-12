numbers = list(map(int, input("Enter sorted numbers: ").split()))
target = int(input("Enter target: "))

closest = numbers[0]

for number in numbers:
    if abs(number - target) < abs(closest - target):
        closest = number

print("Nearest number:", closest)