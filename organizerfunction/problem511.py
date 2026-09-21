list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

frequency1 = {}
frequency2 = {}

for number in list1:
    frequency1[number] = frequency1.get(number, 0) + 1

for number in list2:
    frequency2[number] = frequency2.get(number, 0) + 1

if frequency1 == frequency2:
    print("Both lists have the same frequency.")
else:
    print("The lists have different frequencies.")