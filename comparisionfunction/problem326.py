numbers = list(map(int, input("Enter numbers: ").split()))

longest = []
current = [numbers[0]]

for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        current.append(numbers[i])
    else:
        if len(current) > len(longest):
            longest = current
        current = [numbers[i]]

if len(current) > len(longest):
    longest = current

print("Longest increasing subsequence:", longest)