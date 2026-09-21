numbers = list(map(int, input("Enter numbers: ").split()))

found = None

for number in numbers:
    digits = str(abs(number))

    if len(digits) == len(set(digits)):
        found = number
        break

if found is not None:
    print("First number with all different digits:", found)
else:
    print("No such number found.")