list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

if len(list1) == len(list2) and sum(list1) == sum(list2):
    print("Both lists have the same length and sum")
else:
    print("Lists are different")