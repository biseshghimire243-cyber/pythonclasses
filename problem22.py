try:
    day = int(input("Enter day: "))

    if day < 1 or day > 31:
        raise Exception("Invalid day.")

    print("Day:", day)

except Exception as e:
    print(e)