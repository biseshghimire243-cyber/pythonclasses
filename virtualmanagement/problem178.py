number = int(input("Enter a number from 0 to 9: "))

words = [
    "Zero", "One", "Two", "Three", "Four",
    "Five", "Six", "Seven", "Eight", "Nine"
]

if 0 <= number <= 9:
    print("Number in words:", words[number])
else:
    print("Please enter a number from 0 to 9")