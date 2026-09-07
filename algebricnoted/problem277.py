time = input("Enter time in HH:MM format: ")

parts = time.split(":")

if len(parts) == 2 and all(part.isdigit() for part in parts):
    hour = int(parts[0])
    minute = int(parts[1])

    if 0 <= hour <= 23 and 0 <= minute <= 59:
        print("Valid time")
    else:
        print("Invalid time")
else:
    print("Invalid time format")