# Program to remove duplicates

numbers = list(map(int, input("Enter numbers: ").split()))

unique = list(set(numbers))

print("List without duplicates:", unique)