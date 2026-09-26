numbers = list(map(int, input("Enter numbers: ").split()))

found = None

for number in numbers:
    if "0" in str(abs(number)):
        found = number
        break

if found is not None:
    print("First number containing zero:", found)
else:
    print("No number contains zero")