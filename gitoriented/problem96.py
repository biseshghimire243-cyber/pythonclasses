customers = {}

while True:

    try:

        print("\n========== ELECTRICITY BILLING ==========")
        print("1. Add Customer")
        print("2. Generate Bill")
        print("3. View Customers")
        print("4. Exit")

        choice = int(input("Choice: "))

        if choice == 1:

            meter = input("Meter Number: ")

            name = input("Customer Name: ")

            units = int(input("Units Consumed: "))

            customers[meter] = {
                "Name": name,
                "Units": units
            }

            print("Customer Added.")

        elif choice == 2:

            meter = input("Meter Number: ")

            if meter not in customers:
                raise Exception("Customer Not Found.")

            units = customers[meter]["Units"]

            bill = units * 12

            print("Customer :", customers[meter]["Name"])
            print("Units :", units)
            print("Bill = Rs.", bill)

        elif choice == 3:

            print(customers)

        elif choice == 4:
            break

    except Exception as e:
        print(e)