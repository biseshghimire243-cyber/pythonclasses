try:
    quantity = int(input("Enter product quantity: "))

    if quantity <= 0:
        raise Exception("Quantity must be greater than zero.")

    print("Quantity:", quantity)

except Exception as e:
    print(e)