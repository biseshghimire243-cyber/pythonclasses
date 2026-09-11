numbers = list(map(int, input("Enter numbers: ").split()))

closest = numbers[0]

for number in numbers[1:]:
    if abs(number) < abs(closest):
        closest = number
    elif abs(number) == abs(closest) and number > closest:
        closest = number

print("Number closest to zero:", closest)