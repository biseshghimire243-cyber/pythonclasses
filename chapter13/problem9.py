numbers = [5, 10, 15]

try:
    position = int(input("Enter index: "))
    print(numbers[position])

except IndexError:
    print("Invalid index.")