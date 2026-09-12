list1 = set(map(int, input("Enter first list: ").split()))
list2 = set(map(int, input("Enter second list: ").split()))
list3 = set(map(int, input("Enter third list: ").split()))

result = []

all_numbers = list1 | list2 | list3

for number in all_numbers:
    count = 0

    if number in list1:
        count += 1
    if number in list2:
        count += 1
    if number in list3:
        count += 1

    if count == 2:
        result.append(number)

print("Elements appearing in exactly two lists:", sorted(result))