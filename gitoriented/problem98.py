couriers = {}

while True:

    try:

        print("\n========== COURIER MANAGEMENT ==========")
        print("1. Add Courier")
        print("2. View Couriers")
        print("3. Track Courier")
        print("4. Deliver Courier")
        print("5. Exit")

        choice = int(input("Choice: "))

        if choice == 1:

            tracking = input("Tracking Number: ")

            sender = input("Sender Name: ")
            receiver = input("Receiver Name: ")

            couriers[tracking] = {
                "Sender": sender,
                "Receiver": receiver,
                "Status": "In Transit"
            }

            print("Courier Added.")

        elif choice == 2:

            for tracking, data in couriers.items():

                print(tracking, data)

        elif choice == 3:

            tracking = input("Tracking Number: ")

            if tracking not in couriers:
                raise Exception("Tracking Number Not Found.")

            print(couriers[tracking])

        elif choice == 4:

            tracking = input("Tracking Number: ")

            if tracking not in couriers:
                raise Exception("Tracking Number Not Found.")

            couriers[tracking]["Status"] = "Delivered"

            print("Courier Delivered Successfully.")

        elif choice == 5:
            break

    except Exception as e:
        print(e)