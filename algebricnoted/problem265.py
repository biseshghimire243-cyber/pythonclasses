hour = int(input("Enter hour (1-12): "))
minute = int(input("Enter minutes: "))

hour_angle = (hour % 12) * 30 + minute * 0.5
minute_angle = minute * 6

difference = abs(hour_angle - minute_angle)
angle = min(difference, 360 - difference)

print("Angle between hands:", angle, "degrees")