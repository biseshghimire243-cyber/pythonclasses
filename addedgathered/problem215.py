numbers = list(map(int, input("Enter numbers: ").split()))

duplicates = []
seen = set()

for num in numbers:
    if num in seen and num not in duplicates:
        duplicates.append(num)
    else:
        seen.add(num)

if duplicates:
    print("Duplicate numbers:", duplicates)
else:
    print("No duplicate numbers found.")