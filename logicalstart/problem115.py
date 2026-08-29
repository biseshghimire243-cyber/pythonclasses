total_days = int(input("Enter total working days: "))
present_days = int(input("Enter present days: "))

if total_days <= 0:
    print("Invalid total days")
else:
    percentage = (present_days / total_days) * 100

    print("Attendance:", round(percentage, 2), "%")

    if percentage >= 75:
        print("Eligible for examination")
    else:
        print("Not eligible for examination")