total_days = int(input("Enter total class days: "))
present_days = int(input("Enter days present: "))

percentage = (present_days / total_days) * 100

print("Attendance:", percentage, "%")

if percentage >= 75:
    print("Attendance requirement satisfied")
else:
    print("Attendance requirement not satisfied")