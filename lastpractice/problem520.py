numbers = list(map(int, input("Enter numbers: ").split()))

if len(numbers) < 2:
    print("Not enough numbers.")
else:
    smallest = numbers[0]
    result = None

    for number in numbers[1:]:
        if number < smallest:
            result = number
            break

        if number < smallest:
            smallest = number

    if result is not None:
        print("First number smaller than all previous numbers:", result)
    else:
        print("No such number found.")