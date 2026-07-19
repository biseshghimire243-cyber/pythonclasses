try:
    fruits = ["Apple", "Banana", "Mango"]

    index = int(input("Enter index: "))

    print(fruits[index])

except IndexError:
    print("Index out of range.")