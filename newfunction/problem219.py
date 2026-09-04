list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

intersection = []

for num in list1:
    if num in list2 and num not in intersection:
        intersection.append(num)

print("Intersection:", intersection)