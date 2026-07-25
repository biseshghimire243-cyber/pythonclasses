age = int(input("Enter age: "))

try:
    if age < 18:
        raise Exception("You are not eligible.")

    print("You are eligible.")

except Exception as e:
    print(e)