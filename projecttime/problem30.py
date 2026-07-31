try:
    roll = int(input("Enter roll number: "))

    if roll <= 0:
        raise Exception("Roll number must be positive.")

    print("Roll Number:", roll)

except Exception as e:
    print(e)