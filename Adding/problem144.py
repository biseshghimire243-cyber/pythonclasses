class Loan:

    def __init__(self, customer, amount, rate, years):
        self.customer = customer
        self.amount = amount
        self.rate = rate
        self.years = years

    def calculate_interest(self):
        return self.amount * self.rate * self.years / 100

    def calculate_total(self):
        return self.amount + self.calculate_interest()

    def show_details(self):
        interest = self.calculate_interest()
        total = self.calculate_total()

        print("\n========== LOAN DETAILS ==========")
        print("Customer:", self.customer)
        print("Loan Amount: Rs.", self.amount)
        print("Interest: Rs.", interest)
        print("Total Payment: Rs.", total)


try:
    name = input("Customer Name: ")
    amount = float(input("Loan Amount: "))
    rate = float(input("Interest Rate (%): "))
    years = int(input("Loan Period (years): "))

    if amount <= 0 or rate < 0 or years <= 0:
        raise ValueError("Invalid loan information.")

    loan = Loan(name, amount, rate, years)

    loan.show_details()

except ValueError as e:
    print("Error:", e)