list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

difference = min(abs(a - b) for a in list1 for b in list2)

print("Smallest difference:", difference)