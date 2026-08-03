try:
    rooms = int(input("Enter number of rooms: "))

    if rooms <= 0:
        raise Exception("You must book at least one room.")

    print("Booking Confirmed")

except Exception as e:
    print(e)