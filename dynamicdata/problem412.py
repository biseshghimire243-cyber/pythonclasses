days = int(input("Enter number of working days: "))

total_hours = 0

for i in range(days):
    hours = float(input(f"Hours worked on day {i + 1}: "))
    total_hours += hours

print("Total working hours:", total_hours)
print("Average hours per day:", total_hours / days)