numbers = list(map(int, input("Enter numbers: ").split()))

if numbers:
    current_sum = numbers[0]
    maximum_sum = numbers[0]

    for num in numbers[1:]:
        current_sum = max(num, current_sum + num)
        maximum_sum = max(maximum_sum, current_sum)

    print("Maximum subarray sum:", maximum_sum)
else:
    print("List is empty.")