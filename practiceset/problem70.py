try:
    units = int(input("Enter electricity units: "))

    if units < 0:
        raise Exception("Units cannot be negative.")

    bill = units * 12

    print("Total Bill = Rs.", bill)

except Exception as e:
    print(e)