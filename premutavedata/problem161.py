numbers = [2, 4, 6, 8, 10]

difference = numbers[1] - numbers[0]
arithmetic = True

for i in range(1, len(numbers)):
    if numbers[i] - numbers[i - 1] != difference:
        arithmetic = False
        break

if arithmetic:
    print("Numbers form an arithmetic sequence")
else:
    print("Numbers do not form an arithmetic sequence")