# Program to find second largest number

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

numbers.sort()

print("Second Largest =", numbers[-2])