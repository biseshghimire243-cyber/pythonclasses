numbers = list(map(int, input("Enter numbers: ").split()))

if numbers:
    average = sum(numbers) / len(numbers)
    found = None

    for number in numbers:
        if number > average:
            found = number
            break

    print("Average:", round(average, 2))

    if found is not None:
        print("First number greater than average:", found)
    else:
        print("No number is greater than average.")
else:
    print("No numbers entered.")