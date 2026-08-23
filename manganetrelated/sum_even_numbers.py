name = input("Enter student name: ")
total = int(input("Enter total classes: "))
present = int(input("Enter classes attended: "))

percentage = (present / total) * 100

print("\n===== ATTENDANCE REPORT =====")
print("Student:", name)
print("Total Classes:", total)
print("Present:", present)
print("Attendance:", round(percentage, 2), "%")

if percentage >= 75:
    print("Status: Eligible")
else:
    print("Status: Not Eligible")