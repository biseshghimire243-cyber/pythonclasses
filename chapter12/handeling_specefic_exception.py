try:
    num = int(input("Enter a number: "))
    print(10 / num)

except ZeroDivisionError:
    print("You cannot divide by zero.")