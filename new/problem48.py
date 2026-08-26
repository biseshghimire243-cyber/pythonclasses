numbers = [15, 28, 36, 42, 57, 63, 79]

search = int(input("Enter number to search: "))

if search in numbers:
    position = numbers.index(search)

    print("Number found!")
    print("Position:", position)
else:
    print("Number not found")