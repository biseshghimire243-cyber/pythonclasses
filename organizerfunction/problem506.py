numbers = list(map(int, input("Enter numbers: ").split()))
limit = int(input("Enter limit: "))

longest = 0
current = 0

for number in numbers:
    if number < limit:
        current += 1
        longest = max(longest, current)
    else:
        current = 0

print("Longest sequence below limit:", longest)