list1 = input("Enter first list: ").split()
list2 = input("Enter second list: ").split()

result = []
length = max(len(list1), len(list2))

for i in range(length):
    if i < len(list1):
        result.append(list1[i])

    if i < len(list2):
        result.append(list2[i])

print("Merged list:", result)