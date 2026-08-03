try:
    account = input("Enter account number: ")

    if len(account) != 10 or not account.isdigit():
        raise Exception("Invalid account number.")

    print("Account Number:", account)

except Exception as e:
    print(e)