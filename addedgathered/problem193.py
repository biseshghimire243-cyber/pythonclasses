numbers = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter number to search: "))

count = numbers.count(target)

print("Number of occurrences:", count)