try:
    num = int(input("Enter a number: "))
    print("Square =", num * num)

except ValueError:
    print("Invalid input.")

else:
    print("Program executed successfully.")