try:
    price = float(input("Enter product price: "))

    if price <= 0:
        raise Exception("Price must be greater than zero.")

    print("Price:", price)

except Exception as e:
    print(e)