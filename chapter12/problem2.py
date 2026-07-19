try:
    numbers = [10, 20, 30]

    index = int(input("Enter index: "))
    print("Value =", numbers[index])

except ValueError:
    print("Error: Enter a valid number.")

except IndexError:
    print("Error: Index out of range.")