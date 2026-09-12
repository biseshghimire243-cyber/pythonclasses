numbers = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target: "))

found = False

for number in numbers:
    if number > target:
        print("First number greater than target:", number)
        found = True
        break

if not found:
    print("No number greater than target")