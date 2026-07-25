try:
    number = int(input("Enter a number: "))
    print(100 / number)

except Exception as e:
    print("Error:", e)