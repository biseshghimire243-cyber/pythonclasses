try:
    temp = float(input("Enter temperature: "))

    if temp < -273.15:
        raise Exception("Temperature cannot be below absolute zero.")

    print("Temperature:", temp)

except Exception as e:
    print(e)