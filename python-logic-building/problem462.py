numbers = list(map(int, input("Enter numbers: ").split()))
k = int(input("Enter rotation count: "))

if numbers:
    k = k % len(numbers)
    result = numbers[k:] + numbers[:k]
    print("Rotated list:", result)
else:
    print("List is empty")