try:
    discount = float(input("Enter discount percentage: "))

    if discount < 0 or discount > 100:
        raise Exception("Discount must be between 0 and 100.")

    print("Discount:", discount, "%")

except Exception as e:
    print(e)