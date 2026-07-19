try:
    num = int(input("Enter a number: "))
    print(10 / num)

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Program executed successfully.")