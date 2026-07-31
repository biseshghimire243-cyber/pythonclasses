try:
    username = input("Enter username: ")

    if username == "":
        raise Exception("Username cannot be empty.")

    print("Welcome,", username)

except Exception as e:
    print(e)