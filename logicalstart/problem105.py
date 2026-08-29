binary1 = input("Enter first binary number: ")
binary2 = input("Enter second binary number: ")

decimal1 = int(binary1, 2)
decimal2 = int(binary2, 2)

result = decimal1 + decimal2

print("Binary Sum:", bin(result)[2:])