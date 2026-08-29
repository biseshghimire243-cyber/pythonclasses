day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

valid = True

if month < 1 or month > 12:
    valid = False
else:
    days = [31, 28, 31, 30, 31, 30,
            31, 31, 30, 31, 30, 31]

    if month == 2:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            max_days = 29
        else:
            max_days = 28
    else:
        max_days = days[month - 1]

    if day < 1 or day > max_days:
        valid = False

if valid:
    print("Valid date")
else:
    print("Invalid date")