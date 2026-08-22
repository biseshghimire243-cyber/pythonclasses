start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

for number in range(start, end + 1):
    print("\nTable of", number)

    for i in range(1, 11):
        print(number, "x", i, "=", number * i)