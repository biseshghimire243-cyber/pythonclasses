try:
    quantity = int(input("Enter quantity: "))

    if quantity <= 0:
        raise Exception("Quantity must be greater than zero.")

    print("Quantity:", quantity)

except Exception as e:
    print(e)