try:
    amount = float(input("Enter payment amount: "))

    if amount <= 0:
        raise Exception("Payment amount must be greater than zero.")

    print("Payment Successful")

except Exception as e:
    print(e)