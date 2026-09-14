seconds = int(input("Enter seconds: "))

days = seconds // 86400
remaining = seconds % 86400

hours = remaining // 3600
remaining %= 3600

minutes = remaining // 60
seconds_left = remaining % 60

print("Days:", days)
print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds_left)