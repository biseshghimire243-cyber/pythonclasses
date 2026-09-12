hour1 = int(input("Enter first hour: "))
minute1 = int(input("Enter first minute: "))

hour2 = int(input("Enter second hour: "))
minute2 = int(input("Enter second minute: "))

time1 = hour1 * 60 + minute1
time2 = hour2 * 60 + minute2

difference = abs(time2 - time1)

hours = difference // 60
minutes = difference % 60

print("Time difference:", hours, "hours", minutes, "minutes")