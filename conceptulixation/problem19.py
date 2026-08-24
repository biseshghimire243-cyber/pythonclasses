total_classes = int(input("Enter total classes: "))
present_classes = int(input("Enter present classes: "))

percentage = (present_classes / total_classes) * 100

print("Attendance:", round(percentage, 2), "%")

if percentage >= 75:
    print("Eligible")
else:
    print("Not Eligible")