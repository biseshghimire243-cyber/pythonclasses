current = float(input("Enter current month's units: "))
previous = float(input("Enter previous month's units: "))

if current > previous:
    increase = current - previous
    print("Usage increased by", increase, "units")

elif current < previous:
    decrease = previous - current
    print("Usage decreased by", decrease, "units")

else:
    print("Usage is unchanged")