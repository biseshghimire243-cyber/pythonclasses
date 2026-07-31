try:
    year = int(input("Enter year: "))

    if year < 1900 or year > 2100:
        raise Exception("Invalid year.")

    print("Year:", year)

except Exception as e:
    print(e)