numbers = list(map(int, input("Enter numbers: ").split()))

found = False

for number in numbers:
    if number % 2 == 0:
        print("First even number:", number)
        found = True
        break

if not found:
    print("No even number found")