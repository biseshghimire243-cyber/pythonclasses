def is_leap_year(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

year = int(input("Enter year: "))

if is_leap_year(year):
    print("Leap year")
else:
    print("Not a leap year")