try:
    email = input("Enter email: ")

    if "@" not in email:
        raise Exception("Invalid email address.")

    print("Email Accepted")

except Exception as e:
    print(e)