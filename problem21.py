try:
    month = int(input("Enter month (1-12): "))

    if month < 1 or month > 12:
        raise ValueError("Invalid month.")

    print("Month:", month)

except ValueError as e:
    print(e)