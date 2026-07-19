try:
    number = int(input("Enter a number: "))
    print("You entered:", number)

except ValueError:
    print("Only numbers are allowed.")