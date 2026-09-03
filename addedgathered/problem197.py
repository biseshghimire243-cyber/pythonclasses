list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

if sorted(list1) == sorted(list2):
    print("Both lists contain the same elements.")
else:
    print("Lists contain different elements.")