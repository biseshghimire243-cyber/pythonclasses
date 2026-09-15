numbers = list(map(int, input("Enter numbers: ").split()))

found = False

for number in numbers:
    if number % 7 == 0:
        print("First number divisible by 7:", number)
        found = True
        break

if not found:
    print("No number divisible by 7 found")