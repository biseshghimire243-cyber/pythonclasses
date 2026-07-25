try:
    print("Opening file...")
    number = int(input("Enter number: "))
    print(50 / number)

except ZeroDivisionError:
    print("Cannot divide by zero.")

finally:
    print("Closing program...")