numbers = list(map(int, input("Enter numbers: ").split()))
k = int(input("Enter rotation count: "))

if numbers:
    k = k % len(numbers)
    rotated = numbers[-k:] + numbers[:-k] if k else numbers
    print("Rotated list:", rotated)
else:
    print("List is empty.")