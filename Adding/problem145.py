class Student:

    def __init__(self, name, roll, fee):
        self.name = name
        self.roll = roll
        self.fee = fee
        self.paid = 0

    def pay_fee(self, amount):

        if amount <= 0:
            raise ValueError("Invalid payment.")

        if self.paid + amount > self.fee:
            raise ValueError("Payment exceeds total fee.")

        self.paid += amount

        print("Fee payment successful.")

    def show_status(self):

        remaining = self.fee - self.paid

        print("\n========== FEE STATUS ==========")
        print("Name:", self.name)
        print("Roll:", self.roll)
        print("Total Fee: Rs.", self.fee)
        print("Paid: Rs.", self.paid)
        print("Remaining: Rs.", remaining)


students = {}

while True:

    try:

        print("\n1. Add Student")
        print("2. Pay Fee")
        print("3. View Fee Status")
        print("4. Exit")

        choice = int(input("Choice: "))

        if choice == 1:

            roll = input("Roll Number: ")

            if roll in students:
                raise ValueError("Student already exists.")

            name = input("Student Name: ")
            fee = float(input("Total Fee: "))

            students[roll] = Student(
                name,
                roll,
                fee
            )

            print("Student added.")

        elif choice == 2:

            roll = input("Roll Number: ")

            if roll not in students:
                raise ValueError("Student not found.")

            amount = float(input("Payment: "))

            students[roll].pay_fee(amount)

        elif choice == 3:

            roll = input("Roll Number: ")

            if roll not in students:
                raise ValueError("Student not found.")

            students[roll].show_status()

        elif choice == 4:
            break

        else:
            print("Invalid choice.")

    except ValueError as e:
        print("Error:", e)