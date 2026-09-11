def divisor_sum(number):
    total = 0

    for i in range(1, number):
        if number % i == 0:
            total += i

    return total


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if divisor_sum(a) == b and divisor_sum(b) == a:
    print("Amicable numbers")
else:
    print("Not amicable numbers")