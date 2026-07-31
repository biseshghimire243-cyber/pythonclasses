try:
    fruits = ["Apple", "Banana", "Mango"]

    fruit = input("Enter fruit name: ")

    if fruit not in fruits:
        raise Exception("Fruit not found.")

    print(fruit, "is available.")

except Exception as e:
    print(e)