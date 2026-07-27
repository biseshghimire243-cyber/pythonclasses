correct_password = "python123"

for attempt in range(3):
    password = input("Enter password: ")

    if password == correct_password:
        print("Login Successful")
        break
else:
    print("Account Locked")