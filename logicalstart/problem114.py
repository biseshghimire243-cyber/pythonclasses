from datetime import date

year1 = int(input("Enter first year: "))
month1 = int(input("Enter first month: "))
day1 = int(input("Enter first day: "))

year2 = int(input("Enter second year: "))
month2 = int(input("Enter second month: "))
day2 = int(input("Enter second day: "))

date1 = date(year1, month1, day1)
date2 = date(year2, month2, day2)

difference = abs((date2 - date1).days)

print("Number of days:", difference)