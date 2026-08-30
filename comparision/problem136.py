date1 = input("Enter first date (YYYY-MM-DD): ")
date2 = input("Enter second date (YYYY-MM-DD): ")

if date1 > date2:
    print("First date is later")
elif date1 < date2:
    print("Second date is later")
else:
    print("Both dates are the same")