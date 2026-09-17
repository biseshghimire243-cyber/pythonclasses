numbers = list(map(int, input("Enter numbers: ").split()))

sorted_numbers = sorted(set(numbers))

for number in numbers:
    rank = sorted_numbers.index(number) + 1
    print(number, "-> Rank", rank)