hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))

regular_hours = min(hours, 40)
overtime_hours = max(hours - 40, 0)

regular_pay = regular_hours * rate
overtime_pay = overtime_hours * rate * 1.5

total_pay = regular_pay + overtime_pay

print("Regular pay:", regular_pay)
print("Overtime pay:", overtime_pay)
print("Total pay:", total_pay)