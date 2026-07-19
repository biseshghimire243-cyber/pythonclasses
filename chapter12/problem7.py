try:
    password = input("Enter password: ")

    if password != "python123":
        raise Exception("Incorrect Password")

    print("Login Successful")

except Exception as e:
    print(e)