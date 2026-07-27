try:
    number = int(input("Enter a number: "))

    if number % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

except ValueError:
    print("Please enter a valid integer.")