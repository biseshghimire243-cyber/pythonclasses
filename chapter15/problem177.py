class LoginError(Exception):
    pass


class LoginSystem:

    def __init__(self):

        self.users = {
            "admin": "1234",
            "bishesh": "python123"
        }

    def login(self, username, password):

        if username not in self.users:

            raise LoginError(
                "Username does not exist."
            )

        if self.users[username] != password:

            raise LoginError(
                "Incorrect password."
            )

        print("Login successful!")
        print("Welcome,", username)


system = LoginSystem()

attempts = 3

while attempts > 0:

    try:

        username = input("Username: ")
        password = input("Password: ")

        system.login(
            username,
            password
        )

        break

    except LoginError as error:

        attempts -= 1

        print("Error:", error)
        print(
            "Attempts remaining:",
            attempts
        )

else:

    print("Account locked.")