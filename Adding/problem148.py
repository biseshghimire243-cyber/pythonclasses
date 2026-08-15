class Package:

    def __init__(self, tracking_id, sender, receiver):
        self.tracking_id = tracking_id
        self.sender = sender
        self.receiver = receiver
        self.status = "Processing"

    def update_status(self, status):

        valid_status = [
            "Processing",
            "Shipped",
            "Out for Delivery",
            "Delivered"
        ]

        if status not in valid_status:
            raise ValueError("Invalid status.")

        self.status = status

        print("Status updated.")

    def show_tracking(self):

        print("\n========== TRACKING ==========")
        print("Tracking ID:", self.tracking_id)
        print("Sender:", self.sender)
        print("Receiver:", self.receiver)
        print("Status:", self.status)


packages = {}

while True:

    try:

        print("\n1. Add Package")
        print("2. Update Status")
        print("3. Track Package")
        print("4. Exit")

        choice = int(input("Choice: "))

        if choice == 1:

            tracking = input("Tracking ID: ")

            if tracking in packages:
                raise ValueError("Package already exists.")

            sender = input("Sender: ")
            receiver = input("Receiver: ")

            packages[tracking] = Package(
                tracking,
                sender,
                receiver
            )

            print("Package registered.")

        elif choice == 2:

            tracking = input("Tracking ID: ")

            if tracking not in packages:
                raise ValueError("Package not found.")

            print("Processing")
            print("Shipped")
            print("Out for Delivery")
            print("Delivered")

            status = input("New Status: ")

            packages[tracking].update_status(status)

        elif choice == 3:

            tracking = input("Tracking ID: ")

            if tracking not in packages:
                raise ValueError("Package not found.")

            packages[tracking].show_tracking()

        elif choice == 4:
            break

        else:
            print("Invalid choice.")

    except ValueError as e:
        print("Error:", e)