pets = {}

while True:

    try:

        print("\n========== PET SHOP ==========")
        print("1. Add Pet")
        print("2. View Pets")
        print("3. Sell Pet")
        print("4. Search Pet")
        print("5. Exit")

        choice = int(input("Choice: "))

        if choice == 1:

            pet = input("Pet Name: ")
            price = float(input("Price: "))

            pets[pet] = price

            print("Pet Added.")

        elif choice == 2:

            for pet, price in pets.items():

                print(pet, "-", price)

        elif choice == 3:

            pet = input("Pet Name: ")

            if pet not in pets:
                raise Exception("Pet Not Found.")

            del pets[pet]

            print("Pet Sold Successfully.")

        elif choice == 4:

            pet = input("Pet Name: ")

            if pet not in pets:
                raise Exception("Pet Not Found.")

            print("Price =", pets[pet])

        elif choice == 5:
            break

    except Exception as e:
        print(e)