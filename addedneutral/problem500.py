numbers = list(map(int, input("Enter numbers: ").split()))

seen = set()
repeated = None

for number in numbers:
    if number in seen:
        repeated = number
        break

    seen.add(number)

if repeated is not None:
    print("First repeated number:", repeated)
else:
    print("No repeated number found.")