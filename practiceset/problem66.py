try:
    age = int(input("Enter employee age: "))

    if age < 18 or age > 60:
        raise Exception("Employee age must be between 18 and 60.")

    print("Employee Age:", age)

except Exception as e:
    print(e)