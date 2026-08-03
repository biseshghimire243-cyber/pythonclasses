try:
    phone = input("Enter phone number: ")

    if len(phone) != 10:
        raise Exception("Phone number must contain 10 digits.")

    print("Phone Number:", phone)

except Exception as e:
    print(e)