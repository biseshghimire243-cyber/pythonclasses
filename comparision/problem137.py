speed1 = float(input("Enter first internet speed: "))
speed2 = float(input("Enter second internet speed: "))

if speed1 > speed2:
    print("Internet 1 is faster")
elif speed2 > speed1:
    print("Internet 2 is faster")
else:
    print("Both speeds are equal")