minutes = int(input("Enter total minutes: "))

days = minutes // (24 * 60)
remaining = minutes % (24 * 60)

hours = remaining // 60
minutes_left = remaining % 60

print("Days:", days)
print("Hours:", hours)
print("Minutes:", minutes_left)