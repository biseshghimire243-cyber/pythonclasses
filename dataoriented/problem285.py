seconds = int(input("Enter total seconds: "))

weeks = seconds // 604800
seconds %= 604800

days = seconds // 86400
seconds %= 86400

hours = seconds // 3600
seconds %= 3600

minutes = seconds // 60
seconds %= 60

print("Weeks:", weeks)
print("Days:", days)
print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)