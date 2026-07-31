try:
    username = input("Enter username: ")

    if len(username) < 5:
        raise Exception("Username must contain at least 5 characters.")

    print("Username:", username)

except Exception as e:
    print(e)