start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
limit = int(input("Enter table limit: "))

for number in range(start, end + 1):
    print(f"\nTable of {number}")

    for i in range(1, limit + 1):
        print(f"{number} x {i} = {number * i}")