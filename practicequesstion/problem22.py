try:
    password = input("Enter password: ")

    if len(password) < 8:
        raise Exception("Password must contain at least 8 characters.")

    print("Password accepted.")

except Exception as e:
    print(e)