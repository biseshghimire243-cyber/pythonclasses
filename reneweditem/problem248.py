numbers = list(map(int, input("Enter numbers: ").split()))
k = int(input("Enter k: "))

unique = sorted(set(numbers), reverse=True)

if 1 <= k <= len(unique):
    print("Kth largest element:", unique[k - 1])
else:
    print("Invalid k value.")