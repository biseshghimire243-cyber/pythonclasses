numbers = list(map(int, input("Enter numbers: ").split()))
k = int(input("Enter k: "))

unique = sorted(set(numbers))

if 1 <= k <= len(unique):
    print("Kth smallest element:", unique[k - 1])
else:
    print("Invalid k value.")