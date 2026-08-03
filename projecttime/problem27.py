try:
    pin = input("Enter 4-digit PIN: ")

    if len(pin) != 4 or not pin.isdigit():
        raise Exception("Invalid PIN.")

    print("PIN Accepted")

except Exception as e:
    print(e)